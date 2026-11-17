"""Deterministic ancilla-free three-qubit chiral-filter compiler.

Qubit 0 is the most significant bit. Matrix products act on column vectors;
the returned gate list is chronological (its first gate acts first).
Gate set: arbitrary one-qubit unitary matrices and CNOT. A single global
phase is returned separately and has no effect on the instrument.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

import numpy as np

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)


def intertwiners():
    a = np.zeros((2, 8), dtype=complex)
    a[0, 2], a[0, 4] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    a[1, 3], a[1, 5] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    b = np.zeros((2, 8), dtype=complex)
    b[0, 1] = np.sqrt(2 / 3)
    b[0, [2, 4]] = -1 / np.sqrt(6)
    b[1, 6] = -np.sqrt(2 / 3)
    b[1, [3, 5]] = 1 / np.sqrt(6)
    return a, b


def local_unitary():
    a, b = intertwiners()
    symmetric = np.zeros((4, 8), dtype=complex)
    symmetric[0, 0] = symmetric[3, 7] = 1
    symmetric[1, [1, 2, 4]] = 1 / np.sqrt(3)
    symmetric[2, [3, 5, 6]] = 1 / np.sqrt(3)
    return np.vstack(((a + 1j * b) / np.sqrt(2),
                      (a - 1j * b) / np.sqrt(2), symmetric))


def one_gate(qubit, matrix, label="U"):
    return {"kind": "one", "qubit": int(qubit), "label": label,
            "matrix": np.asarray(matrix, dtype=complex)}


def cx(control, target):
    return {"kind": "cx", "control": int(control), "target": int(target)}


def rz(angle):
    return np.diag([np.exp(-0.5j * angle), np.exp(0.5j * angle)])


def ry(angle):
    c, s = np.cos(angle / 2), np.sin(angle / 2)
    return np.array([[c, -s], [s, c]], dtype=complex)


def gate_matrix(gate):
    if gate["kind"] == "one":
        matrix = np.ones((1, 1), dtype=complex)
        for qubit in range(3):
            matrix = np.kron(matrix, gate["matrix"] if qubit == gate["qubit"] else I2)
        return matrix
    matrix = np.zeros((8, 8), dtype=complex)
    for index in range(8):
        output = index
        if (index >> (2 - gate["control"])) & 1:
            output ^= 1 << (2 - gate["target"])
        matrix[output, index] = 1
    return matrix


def inverse(gates):
    return [one_gate(g["qubit"], g["matrix"].conj().T, g["label"] + "†")
            if g["kind"] == "one" else dict(g) for g in reversed(gates)]


def product(gates):
    result = np.eye(8, dtype=complex)
    for gate in gates:
        result = gate_matrix(gate) @ result
    return result


def su2_euler(unitary):
    """Return alpha, theta, beta with U=Rz(alpha) Ry(theta) Rz(beta)."""
    u = np.asarray(unitary)
    theta = 2 * np.arctan2(abs(u[1, 0]), abs(u[0, 0]))
    if abs(u[1, 0]) < 1e-13:
        alpha, beta = -2 * np.angle(u[0, 0]), 0.0
    elif abs(u[0, 0]) < 1e-13:
        alpha, beta = 2 * np.angle(u[1, 0]), 0.0
    else:
        alpha = np.angle(u[1, 0]) - np.angle(u[0, 0])
        beta = -np.angle(u[1, 0]) - np.angle(u[0, 0])
    reconstructed = rz(alpha) @ ry(theta) @ rz(beta)
    if np.linalg.norm(reconstructed - u) > 1e-10:
        raise ValueError("SU(2) Euler decomposition failed")
    return alpha, theta, beta


def controlled_su2(control, target, unitary):
    """Two CNOTs and three one-qubit matrices, with no hidden phase."""
    alpha, theta, beta = su2_euler(unitary)
    a = rz(alpha) @ ry(theta / 2)
    b = ry(-theta / 2) @ rz(-(alpha + beta) / 2)
    c = rz((beta - alpha) / 2)
    assert np.linalg.norm(a @ b @ c - I2) < 1e-10
    assert np.linalg.norm(a @ X @ b @ X @ c - unitary) < 1e-10
    return [one_gate(target, c, "C"), cx(control, target),
            one_gate(target, b, "B"), cx(control, target),
            one_gate(target, a, "A")]


def su2_root(unitary):
    trace = float(np.trace(unitary).real)
    if 2 + trace < 1e-12:
        return np.diag([1j, -1j])
    root = (unitary + I2) / np.sqrt(2 + trace)
    assert np.linalg.norm(root @ root - unitary) < 1e-10
    return root


def twice_controlled_su2(unitary):
    """Controls 0,1 on |11>, target 2; 8 CNOT and 9 one-qubit gates."""
    v = su2_root(unitary)
    return (controlled_su2(1, 2, v) + [cx(0, 1)]
            + controlled_su2(1, 2, v.conj().T) + [cx(0, 1)]
            + controlled_su2(0, 2, v))


def affine_to_zero_one(left, right):
    """Known X/CNOT permutation P taking left->000 and right->001."""
    gates = []
    for qubit in range(3):
        if (left >> (2 - qubit)) & 1:
            gates.append(one_gate(qubit, X, "X"))
    difference = left ^ right
    pivot = next(q for q in range(3) if (difference >> (2 - q)) & 1)
    if pivot != 2:
        gates += [cx(pivot, 2), cx(2, pivot), cx(pivot, 2)]
        bit_p, bit_t = (difference >> (2 - pivot)) & 1, difference & 1
        if bit_p != bit_t:
            difference ^= (1 << (2 - pivot)) | 1
    for qubit in (0, 1):
        if (difference >> (2 - qubit)) & 1:
            gates.append(cx(2, qubit))
    p = product(gates)
    assert np.argmax(abs(p[:, left])) == 0
    assert np.argmax(abs(p[:, right])) == 1
    return gates


def compile_two_level(left, right, unitary):
    p = affine_to_zero_one(left, right)
    flip_controls = [one_gate(0, X, "X"), one_gate(1, X, "X")]
    return (p + flip_controls + twice_controlled_su2(unitary)
            + inverse(flip_controls) + inverse(p))


def compile_diagonal(phases):
    """Walsh expansion of a three-qubit diagonal phase gate."""
    gates = []
    coefficients = []
    for mask in range(8):
        theta = sum(phases[x] * (-1) ** ((mask & x).bit_count()) for x in range(8)) / 8
        coefficients.append(theta)
        if mask == 0:
            continue
        qubits = [q for q in range(3) if (mask >> (2 - q)) & 1]
        target = qubits[-1]
        parity = [cx(q, target) for q in qubits[:-1]]
        gates += parity + [one_gate(target, rz(-2 * theta), "Rz")] + inverse(parity)
    return coefficients[0], gates


def compile_circuit():
    w = local_unitary()
    m, eliminations = w.copy(), []
    for column in range(7):
        for row in range(7, column, -1):
            if abs(m[row, column]) < 1e-13:
                continue
            a, b = m[row - 1, column], m[row, column]
            norm = np.sqrt(abs(a) ** 2 + abs(b) ** 2)
            g = np.array([[a.conjugate(), b.conjugate()], [-b, a]]) / norm
            m[[row - 1, row], :] = g @ m[[row - 1, row], :]
            eliminations.append((row - 1, row, g))
    if np.linalg.norm(m - np.diag(np.diag(m))) > 1e-11:
        raise ValueError("QR elimination did not diagonalize W")
    phase, gates = compile_diagonal(np.angle(np.diag(m)))
    for left, right, g in reversed(eliminations):
        gates += compile_two_level(left, right, g.conj().T)
    reconstruction = np.exp(1j * phase) * product(gates)
    residual = float(np.linalg.norm(reconstruction - w))
    if residual > 1e-10:
        raise ValueError(f"Full circuit residual {residual}")
    counts = Counter(g["kind"] for g in gates)
    return {"global_phase": float(phase), "gates": gates,
            "two_level_factors": len(eliminations),
            "counts": dict(counts), "reconstruction_error": residual}


def serializable(circuit):
    result = {k: v for k, v in circuit.items() if k != "gates"}
    result["qubit_order"] = "q0 q1 q2, q0 most significant"
    result["execution_order"] = "chronological"
    result["gates"] = []
    for gate in circuit["gates"]:
        g = dict(gate)
        if g["kind"] == "one":
            u = g.pop("matrix")
            g["real"], g["imag"] = u.real.tolist(), u.imag.tolist()
        result["gates"].append(g)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path, help="Optional chronological JSON gate list")
    args = parser.parse_args()
    circuit = compile_circuit()
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(json.dumps(serializable(circuit), indent=2) + "\n")
    print(json.dumps({k: v for k, v in circuit.items() if k != "gates"}, indent=2))
