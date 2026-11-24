#!/usr/bin/env python3
"""Check finite cyclic decoders and exact momentum multiplicity bookkeeping."""

from itertools import product
from math import comb

import numpy as np


I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
PAULIS = (X, Y, Z)
RAISE = (X + 1j * Y) / 2
SINGLET = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)


def kron_all(factors):
    result = np.array(1, dtype=complex)
    for factor in factors:
        result = np.kron(result, factor)
    return result


def on_site(operator, site, n):
    return kron_all(operator if index == site else I for index in range(n))


def shift(vector, n):
    return vector.reshape((2,) * n).transpose((n - 1, *range(n - 1))).ravel()


def normalized(vector):
    norm = np.linalg.norm(vector)
    assert norm > 1e-10
    return vector / norm


def odd_block(n):
    """Choose one spin-half copy and project it to nonzero cyclic momentum."""
    seed = kron_all([SINGLET] * (n // 2) + [np.array([1, 0])])
    translated = [seed]
    for _ in range(n - 1):
        translated.append(shift(translated[-1], n))
    projections = np.fft.fft(np.array(translated), axis=0)
    up = normalized(max(projections, key=np.linalg.norm))
    lower = sum(on_site(RAISE.conj().T, index, n) for index in range(n))
    return np.column_stack((up, normalized(lower @ up)))


def even_block(n):
    """Decode a common spin-zero and spin-one copy at momentum minus one."""
    dimers = kron_all([SINGLET] * (n // 2))
    translated = shift(dimers, n)
    singlet = normalized(dimers - translated)
    raise_odd = sum(on_site(RAISE, index, n) for index in range(0, n, 2))
    up = normalized(raise_odd @ (dimers + translated))
    lower = sum(on_site(RAISE.conj().T, index, n) for index in range(n))
    middle = normalized(lower @ up)
    down = normalized(lower @ middle)
    return np.column_stack((
        up, (middle + singlet) / np.sqrt(2), (middle - singlet) / np.sqrt(2), down
    ))


def check_block(n):
    basis = odd_block(n) if n % 2 else even_block(n)
    rank = basis.shape[1]
    spectator = rank // 2
    decoder = basis.conj().T
    np.testing.assert_allclose(decoder @ basis, np.eye(rank), atol=2e-14)
    shifted = np.column_stack([shift(column, n) for column in basis.T])
    eigenvalue = np.vdot(basis[:, 0], shifted[:, 0])
    np.testing.assert_allclose(shifted, eigenvalue * basis, atol=2e-14)

    for pauli in PAULIS:
        decoded_generator = pauli
        if spectator == 2:
            decoded_generator = np.kron(pauli, I) + np.kron(I, pauli)
        for site in range(n):
            observed = decoder @ on_site(pauli, site, n) @ basis
            np.testing.assert_allclose(observed, decoded_generator / n, atol=2e-14)

    rotation = np.cos(0.37) * I + 1j * np.sin(0.37) * X
    error = (X + 1j * Y + (1 - 1j) * Z) / 2
    target = rotation.ravel() / np.sqrt(2)
    bad_projector = np.eye(4) - np.outer(target, target.conj())
    epsilon = 1e-4
    pure_success = rank / 2**n
    success = bad = 0.0
    for pattern in product((False, True), repeat=n):
        num_errors = sum(pattern)
        raw = kron_all(rotation @ error if site else rotation for site in pattern)
        accepted = decoder @ raw @ basis / np.sqrt(2**n)
        # Group the two decoded target qubits and the two spectator registers.
        accepted = accepted.reshape(2, spectator, 2, spectator)
        accepted = accepted.transpose(0, 2, 1, 3).reshape(4, spectator**2)
        accepted_success = np.linalg.norm(accepted) ** 2
        accepted_bad = np.linalg.norm(bad_projector @ accepted) ** 2
        if num_errors == 0:
            np.testing.assert_allclose(accepted_success, pure_success, atol=2e-14)
            np.testing.assert_allclose(accepted_bad, 0, atol=2e-14)
        elif num_errors == 1:
            np.testing.assert_allclose(accepted_bad, pure_success / n**2, atol=2e-14)
        weight = epsilon**num_errors * (1 - epsilon)**(n - num_errors)
        success += weight * accepted_success
        bad += weight * accepted_bad

    infidelity = bad / success
    lead_term = epsilon * (1 - epsilon)**(n - 1) * pure_success / n / success
    upper = epsilon / (n * (1 - epsilon))
    upper += comb(n, 2) * epsilon**2 / (pure_success * (1 - epsilon)**n)
    assert lead_term - 2e-14 <= infidelity <= upper + 2e-14


def spin_count(n, two_j):
    if two_j < 0 or two_j > n or (n - two_j) % 2:
        return 0
    weight = (n - two_j) // 2
    lower = comb(n, weight - 1) if weight else 0
    return comb(n, weight) - lower


def weight_momentum_counts(n, weight, divisors):
    if weight < 0:
        return [0] * n
    exact_period = {}
    for period in divisors:
        repeat = n // period
        fixed = comb(period, weight // repeat) if weight % repeat == 0 else 0
        exact_period[period] = fixed - sum(
            count for smaller, count in exact_period.items() if period % smaller == 0
        )
        assert exact_period[period] >= 0 and exact_period[period] % period == 0
    return [
        sum(count // period for period, count in exact_period.items() if (q * period) % n == 0)
        for q in range(n)
    ]


def check_multiplicities(n):
    divisors = [period for period in range(1, n + 1) if n % period == 0]
    momentum = [weight_momentum_counts(n, k, divisors) for k in range(n // 2 + 1)]
    # This integer is at least the uniform trace-error bound in the proof.
    buffer = 2 << ((n + 1) // 2)

    def allocation(two_j):
        return max(0, spin_count(n - 1, two_j) // n - buffer)

    dimension = allocated = 0
    for two_j in range(n % 2, n + 1, 2):
        weight = (n - two_j) // 2
        previous = momentum[weight - 1] if weight else [0] * n
        counts = [current - prior for current, prior in zip(momentum[weight], previous)]
        total = spin_count(n, two_j)
        assert sum(counts) == total
        assert total == spin_count(n - 1, two_j - 1) + spin_count(n - 1, two_j + 1)
        requested = allocation(two_j - 1) + allocation(two_j + 1)
        for available in counts:
            assert abs(n * available - total) <= n * buffer
            assert 0 <= requested <= available
            assert available - requested <= 3 * buffer + 2
            dimension += (two_j + 1) * available
            allocated += (two_j + 1) * requested
    assert dimension == 2**n
    return allocated / dimension


def main():
    for n in (3, 4, 5, 6):
        check_block(n)
    for n in range(3, 71):
        success = check_multiplicities(n)
    assert success > 0.99999
    print("Near-pure decoder checks passed for n=3,4,5,6.")
    print(f"Exact cyclic multiplicities checked through n=70 (allocated acceptance {success:.8f}).")


if __name__ == "__main__":
    main()
