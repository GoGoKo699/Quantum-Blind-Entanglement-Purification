#!/usr/bin/env python3
"""Verify the exact compression and worst-case envelope of the three-pair filter."""
from fractions import Fraction
from itertools import product
from math import ceil

import sympy as sp

from check_exact import intertwiners, zero


IDENTITY = sp.eye(2)
PAULIS = (sp.Matrix([[0, 1], [1, 0]]),
          sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.diag(1, -1))
BASIS = (IDENTITY, *PAULIS)
AXES = tuple(sp.eye(3).col(i) for i in range(3))


def spin(vector):
    return sum((coefficient * pauli for coefficient, pauli in zip(vector, PAULIS)), sp.zeros(2))


def expected_compression(labels):
    active = [position for position, label in enumerate(labels) if label]
    if not active:
        return IDENTITY
    if len(active) == 1:
        return BASIS[labels[active[0]]] / 3
    if len(active) == 2:
        first, second = active
        if (second - first) % 3 != 1:
            first, second = second, first
        a, b = AXES[labels[first] - 1], AXES[labels[second] - 1]
        return -a.dot(b) * IDENTITY / 3 - spin(a.cross(b)) / sp.sqrt(3)
    a, b, c = (AXES[label - 1] for label in labels)
    return (-a.dot(b.cross(c)) * IDENTITY / sp.sqrt(3)
            - spin(a * b.dot(c) + b * c.dot(a) + c * a.dot(b)) / 3)


def check_pauli_tensor_basis():
    a, b = intertwiners()
    plus = (a + sp.I * b) / sp.sqrt(2)
    minus = plus.conjugate()
    time_reversal = sp.I * PAULIS[1]
    for labels in product(range(4), repeat=3):
        error = sp.kronecker_product(*(BASIS[label] for label in labels))
        compressed_plus = (plus * error * plus.H).applyfunc(sp.simplify)
        compressed_minus = (minus * error * minus.H).applyfunc(sp.simplify)
        sign = (-1) ** sum(bool(label) for label in labels)
        assert zero(compressed_plus - expected_compression(labels)), labels
        assert zero(time_reversal * compressed_plus.conjugate() * time_reversal.H
                    - sign * compressed_minus), labels
        output_vectors = [sp.Matrix(list(m.T)) for m in (compressed_plus, compressed_minus)]
        output = sum((v * v.H for v in output_vectors), sp.zeros(4)) / 8
        bell = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
        good = (bell.H * output * bell)[0]
        assert zero(output * bell - good * bell), labels
        success = sp.trace(output)
        for remaining in (0, 1):
            marginal = sp.Matrix(2, 2, lambda i, j: sum(
                output[2*i+k, 2*j+k] if remaining == 0 else output[2*k+i, 2*k+j]
                for k in range(2)))
            assert zero(marginal - success * IDENTITY / 2), (labels, remaining)


def check_floor():
    r, squared_sum, triple_product = sp.symbols("r squared_sum triple_product")
    w = 1 - r
    good = w**3/2 + w*r**2*squared_sum/18 + r**3*(1 - squared_sum + 2*triple_product)/6
    error = w**2*r/6 + w*r**2*(3 - squared_sum)/6 + r**3*(squared_sum + 6*triple_product)/18
    factored = r*(1 - 2*r)*((1 - 2*r)*(2 - r) + r*squared_sum - 2*r**2*triple_product)/6
    assert sp.expand(r*good - w*error - factored) == 0
    orthogonal = {squared_sum: 0, triple_product: 0}
    success = sp.factor((good + error).subs(orthogonal))
    assert sp.factor(good + error - success - r**2*(-squared_sum + 6*r*triple_product)/9) == 0
    fidelity = sp.cancel(good.subs(orthogonal) / success)
    assert fidelity.subs(r, sp.Rational(3, 10)) == sp.Rational(22, 29)
    assert success.subs(r, sp.Rational(3, 10)) == sp.Rational(29, 125)
    assert sp.diff(fidelity, r).subs(r, 0) == -sp.Rational(1, 3)
    u = sp.symbols("u")
    ratio_difference = (u + 3*u**2)/(3 + u**3) - 2*u/9 - u**2/3
    assert sp.cancel(9*(3 + u**3)*ratio_difference) == 3*u + 18*u**2 - 2*u**4 - 3*u**5


def check_heterogeneous_budget():
    floor = Fraction(7, 10)
    mean_cap = Fraction(1)
    levels = 0
    while floor < Fraction(99, 100):
        error = 1 - floor
        mean_cap *= 6 / floor**3
        good = 3*floor**3 + error**3
        floor = good / (good + floor**2*error + 3*floor*error**2)
        levels += 1
    assert levels == 6
    assert ceil(2*mean_cap) == 1819301
    assert 5 * ceil(2*mean_cap) == 9096505


if __name__ == "__main__":
    check_pauli_tensor_basis()
    check_floor()
    check_heterogeneous_budget()
    print("PASS: 64 exact Pauli contractions, pooled output invariants, sharp-floor identities, and the finite heterogeneous budget.")
