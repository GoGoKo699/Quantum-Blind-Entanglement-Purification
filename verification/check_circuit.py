"""Consequential checks of the ancilla-free local filter compiler."""
from __future__ import annotations

import json

import numpy as np
import sympy as sp

from chiral_circuit import (
    I2, X, Y, Z, compile_circuit, compile_diagonal, compile_two_level,
    intertwiners, local_unitary, product,
)


def residual(a, b):
    return float(np.linalg.norm(a - b))


def exact_qr():
    """Check the advertised sparse QR pattern without a floating zero cutoff."""
    a = sp.zeros(2, 8)
    for row, plus, minus in ((0, 2, 4), (1, 3, 5)):
        a[row, plus], a[row, minus] = 1 / sp.sqrt(2), -1 / sp.sqrt(2)
    b = sp.zeros(2, 8)
    b[0, 1], b[1, 6] = sp.sqrt(sp.Rational(2, 3)), -sp.sqrt(sp.Rational(2, 3))
    b[0, 2] = b[0, 4] = -1 / sp.sqrt(6)
    b[1, 3] = b[1, 5] = 1 / sp.sqrt(6)
    symmetric = sp.zeros(4, 8)
    symmetric[0, 0] = symmetric[3, 7] = 1
    for index in (1, 2, 4):
        symmetric[1, index] = 1 / sp.sqrt(3)
    for index in (3, 5, 6):
        symmetric[2, index] = 1 / sp.sqrt(3)
    m = ((a + sp.I * b) / sp.sqrt(2)).col_join(
        (a - sp.I * b) / sp.sqrt(2)).col_join(symmetric)
    labels = []
    for column in range(7):
        for row in range(7, column, -1):
            bottom = sp.simplify(m[row, column])
            if bottom == 0:
                continue
            top = sp.simplify(m[row - 1, column])
            norm = sp.sqrt(sp.simplify(abs(top) ** 2 + abs(bottom) ** 2))
            g = sp.Matrix([[sp.conjugate(top), sp.conjugate(bottom)], [-bottom, top]]) / norm
            rows = g * m.extract([row - 1, row], list(range(8)))
            for index in range(8):
                m[row - 1, index] = sp.simplify(rows[0, index])
                m[row, index] = sp.simplify(rows[1, index])
            labels.append((row - 1, row))
    expected = [(3, 4), (2, 3), (1, 2), (0, 1), (4, 5), (3, 4), (2, 3),
                (1, 2), (3, 4), (2, 3), (5, 6), (4, 5), (3, 4), (5, 6)]
    diagonal = [1, 1, 1, 1, -sp.sqrt(3) / 2 - sp.I / 2,
                1, -sp.sqrt(3) / 2 + sp.I / 2, 1]
    assert labels == expected
    assert m == sp.diag(*diagonal)
    return len(labels)


def main():
    a, b = intertwiners()
    cplus, cminus = (a + 1j * b) / np.sqrt(2), (a - 1j * b) / np.sqrt(2)
    w = local_unitary()
    instrument = max(residual(a @ a.conj().T, I2),
                     residual(b @ b.conj().T, I2),
                     residual(a @ b.conj().T, np.zeros((2, 2))),
                     residual(cplus @ cminus.conj().T, np.zeros((2, 2))),
                     residual(w @ w.conj().T, np.eye(8)))
    effects = cplus.conj().T @ cplus + cminus.conj().T @ cminus
    eigenvalues = np.linalg.eigvalsh(np.eye(8) - effects)
    assert np.min(eigenvalues) > -1e-12
    assert residual(effects @ effects, effects) < 1e-12
    assert np.allclose(eigenvalues, [0, 0, 0, 0, 1, 1, 1, 1], atol=1e-12)

    covariance = 0.0
    for pauli in (X, Y, Z):
        collective = sum(np.kron(np.kron(pauli if q == 0 else I2,
                                        pauli if q == 1 else I2),
                                 pauli if q == 2 else I2) for q in range(3))
        for c in (a, b, cplus, cminus):
            covariance = max(covariance, residual(c @ collective, pauli @ c))

    rng = np.random.default_rng(1729)
    two_level = 0.0
    # Every pair of computational labels tests the affine basis change.
    for left in range(8):
        for right in range(left + 1, 8):
            xyz = rng.normal(size=3)
            xyz /= np.linalg.norm(xyz)
            angle = rng.uniform(-np.pi, np.pi)
            u = np.cos(angle) * I2 - 1j * np.sin(angle) * sum(
                x * pauli for x, pauli in zip(xyz, (X, Y, Z)))
            ideal = np.eye(8, dtype=complex)
            ideal[np.ix_([left, right], [left, right])] = u
            compiled = product(compile_two_level(left, right, u))
            two_level = max(two_level, residual(compiled, ideal))
    # Include the square-root and Euler branch endpoints U=+-I, +/-iY.
    for u in (I2, -I2, 1j * Y, -1j * Y):
        ideal = np.eye(8, dtype=complex)
        ideal[np.ix_([2, 7], [2, 7])] = u
        two_level = max(two_level, residual(product(compile_two_level(2, 7, u)), ideal))

    diagonal = 0.0
    for _ in range(10):
        phases = rng.uniform(-np.pi, np.pi, size=8)
        phase, gates = compile_diagonal(phases)
        diagonal = max(diagonal, residual(np.exp(1j * phase) * product(gates),
                                         np.diag(np.exp(1j * phases))))
    circuit = compile_circuit()
    assert instrument < 1e-11
    assert covariance < 1e-11
    assert two_level < 1e-10
    assert diagonal < 1e-10
    assert circuit["counts"] == {"one": 227, "cx": 194}
    assert circuit["reconstruction_error"] < 1e-10
    exact_factors = exact_qr()
    print(json.dumps({"exact_symbolic_QR_factor_count": exact_factors,
                      "instrument_completeness_residual": instrument,
                      "all_three_generator_covariance_residual": covariance,
                      "all_28_label_pair_compilation_max_residual": two_level,
                      "random_diagonal_compilation_max_residual": diagonal,
                      "full_circuit_reconstruction_residual": circuit["reconstruction_error"],
                      "local_circuit_counts": circuit["counts"],
                      "ancillas": 0}, indent=2))


if __name__ == "__main__":
    main()
