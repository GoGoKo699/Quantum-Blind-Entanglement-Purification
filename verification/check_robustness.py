"""Noisy full-instrument checks for the proved continuity bounds.

These checks use complete six-qubit density matrices and independent random
Hermitian perturbations of both local unitaries. They do not infer a hardware
threshold or an arbitrary-error asymptotic law from finite tests.
"""

from __future__ import annotations

import json

import numpy as np
import sympy as sp
from scipy.linalg import expm

from chiral_circuit import local_unitary


def trace_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.svd(matrix, compute_uv=False).sum())


def reorder_pairs_to_labs(matrix: np.ndarray) -> np.ndarray:
    permutation = []
    for a in range(8):
        for b in range(8):
            index = 0
            for shift in (2, 1, 0):
                index = (index << 2) | (((a >> shift) & 1) << 1) | ((b >> shift) & 1)
            permutation.append(index)
    return matrix[np.ix_(permutation, permutation)]


def accepted(matrix: np.ndarray, wa: np.ndarray, wb: np.ndarray) -> np.ndarray:
    output = np.zeros((4, 4), dtype=complex)
    for ca, cb in ((wa[:2], wb[2:4]), (wa[2:4], wb[:2])):
        kraus = np.kron(ca, cb)
        output += kraus @ matrix @ kraus.conj().T
    return output


def random_unitary(rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    q, r = np.linalg.qr(z)
    return q @ np.diag(np.diag(r) / np.abs(np.diag(r)))


def random_generator(rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8))
    h = z + z.conj().T
    return h / np.linalg.norm(h, 2)


def main() -> None:
    p = sp.symbols("p", real=True)
    success = (p + 1) * (2 * p**2 - p + 1) / 8
    gain = p * (1 - p) * (3 * p - 1) / (2 * (2 * p**2 - p + 1))
    assert sp.factor(success * gain - p * (1 - p**2) * (3 * p - 1) / 16) == 0
    assert sp.Rational(11, 14) - sp.Rational(1, 500) / sp.Rational(28, 125) == sp.Rational(87, 112)

    w = local_unitary()
    rng = np.random.default_rng(172026)
    base_phi = np.array([1, 0, 0, 1], complex) / np.sqrt(2)
    cases = 0
    certified_gain_cases = 0
    max_ideal_error = 0.0
    max_bound_slack_ratio = 0.0
    for visibility in (0.36, 0.4, 0.6, 0.8, 0.95, 0.99):
        for trial in range(4):
            u = random_unitary(rng)
            psi = np.kron(np.eye(2), u) @ base_phi
            target = np.outer(psi, psi.conj())
            source = visibility * target + (1 - visibility) * np.eye(4) / 4
            input_state = reorder_pairs_to_labs(np.kron(np.kron(source, source), source))
            sigma = accepted(input_state, w, w)
            s = float(np.trace(sigma).real)
            ideal = sigma / s
            f = visibility * (5 * visibility + 1) / (3 * (2 * visibility**2 - visibility + 1))
            expected = f * target + (1 - f) * np.eye(4) / 4
            max_ideal_error = max(max_ideal_error, trace_norm(ideal - expected))
            assert np.allclose(ideal, expected, atol=3e-13)
            ha, hb = random_generator(rng), random_generator(rng)
            for theta in (1e-5, 1e-4, 1e-3, 5e-3, 2e-2):
                wa = expm(-1j * theta * ha) @ w
                wb = expm(-1j * theta * hb) @ w
                sigma_hat = accepted(input_state, wa, wb)
                s_hat = float(np.trace(sigma_hat).real)
                actual = sigma_hat / s_hat
                e_upper = np.linalg.norm(wa - w, 2) + np.linalg.norm(wb - w, 2)
                # Complete cq output: accepted quantum block plus scalar failure.
                e_state = (trace_norm(sigma_hat - sigma) + abs(s_hat - s)) / 2
                distance = trace_norm(actual - ideal) / 2
                assert e_state <= e_upper + 2e-12
                assert abs(s_hat - s) <= e_state + 2e-12
                assert distance <= e_state / s + 2e-12
                assert s_hat >= s - e_upper - 2e-12
                actual_fidelity = float(np.trace(target @ actual).real)
                ideal_fidelity = (1 + 3 * f) / 4
                assert actual_fidelity >= ideal_fidelity - e_upper / s - 2e-12
                delta_f = visibility * (1 - visibility) * (3 * visibility - 1) / (2 * (2 * visibility**2 - visibility + 1))
                if e_upper < s * delta_f:
                    assert actual_fidelity > (1 + 3 * visibility) / 4
                    certified_gain_cases += 1
                max_bound_slack_ratio = max(max_bound_slack_ratio, distance / (e_upper / s))
                cases += 1

    # A concrete admissible final local error has a nonzero worst-case floor.
    for lam in (0.001, 0.01, 0.1):
        noisy = (1 - lam) * np.outer(base_phi, base_phi.conj()) + lam * np.eye(4) / 4
        assert np.isclose(1 - float((base_phi.conj() @ noisy @ base_phi).real), 3 * lam / 4)

    report = {
        "cases": cases,
        "certified_gain_cases": certified_gain_cases,
        "maximum_ideal_state_trace_norm_residual": max_ideal_error,
        "maximum_observed_distance_to_bound_ratio": max_bound_slack_ratio,
        "scope": "Fixed seeded finite full-density-matrix cases; analytic bounds in science/robustness.md establish the universal statements.",
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
