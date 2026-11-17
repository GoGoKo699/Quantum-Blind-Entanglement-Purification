#!/usr/bin/env python3
"""Finite-cost checks for the three-copy recursive architecture.

These checks do not prove the uniform conditional-history theorem. They check
exact finite budgets, independently reconstructed iid cost probabilities,
their moments, and pathwise accounting in seeded recursive executions.
Only Python's standard library is required.
"""

from __future__ import annotations

import json
import math
import random
from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction


def visibility_map(p):
    return p * (5 * p + 1) / (3 * (2 * p * p - p + 1))


def success(p):
    return (p + 1) * (2 * p * p - p + 1) / 8


def ceil_fraction(x: Fraction) -> int:
    return (x.numerator + x.denominator - 1) // x.denominator


def design(p0: Fraction, epsilon: Fraction, delta: Fraction) -> dict:
    """Exact rational calculation; not a floating-point budget certificate."""
    assert Fraction(1, 3) < p0 <= 1
    assert 0 < epsilon < 1 and 0 < delta < 1
    p = p0
    expected = Fraction(1)
    levels = 0
    while 3 * (1 - p) > 4 * epsilon:
        expected *= 3 / success(p)
        p = visibility_map(p)
        levels += 1
        if levels > 32:
            raise ValueError("Exact rational check exceeds its small-instance scope")
    if not levels:
        return {"levels": 0, "visibility": p, "mean": expected,
                "cap": 1, "runs": 1, "budget": 1}
    cap = ceil_fraction(2 * expected)
    runs, failure_bound = 0, Fraction(1)
    while failure_bound > delta:
        runs += 1
        failure_bound /= 2
    assert expected / cap <= Fraction(1, 2)
    assert failure_bound <= delta
    return {"levels": levels, "visibility": p, "mean": expected,
            "cap": cap, "runs": runs, "budget": cap * runs}


def iid_moments(p0: float, levels: int):
    """Recursion derived from a geometric sum of three iid child costs."""
    p, mean, variance = p0, 1.0, 0.0
    probabilities = []
    for _ in range(levels):
        s = success(p)
        probabilities.append(s)
        variance = 3 * variance / s + (1 - s) * (3 * mean) ** 2 / s ** 2
        mean = 3 * mean / s
        p = visibility_map(p)
    return mean, variance, probabilities


def second_level_distribution(s0: float, s1: float, cutoff: int = 4000):
    """Coefficients of the rational PGF of C_2/3.

    Its PGF is s1*s0^3*t^3 / ((1-(1-s0)t)^3-(1-s1)*s0^3*t^3).
    This reconstructs the full cost law rather than plugging in E_2.
    """
    q0, q1 = 1 - s0, 1 - s1
    coefficients = [0.0] * (cutoff + 1)
    for n in range(3, cutoff + 1):
        coefficients[n] = (
            3 * q0 * coefficients[n - 1]
            - 3 * q0 * q0 * coefficients[n - 2]
            + (q0 ** 3 + q1 * s0 ** 3) * coefficients[n - 3]
            + (s1 * s0 ** 3 if n == 3 else 0)
        )
    assert min(coefficients) >= -1e-14
    return coefficients


def positive_second_level_probability(n: int, s0: float, s1: float):
    """Independent positive sum: a geometric number of negative-binomial costs."""
    return math.fsum(
        s1 * (1 - s1) ** (k - 1)
        * math.comb(n - 1, 3 * k - 1)
        * s0 ** (3 * k) * (1 - s0) ** (n - 3 * k)
        for k in range(1, n // 3 + 1)
    )


@dataclass
class RegisterTracker:
    acquired: int = 0
    successful: int = 0
    rejected: int = 0
    live: int = 0
    peak: int = 0

    def acquire(self):
        self.acquired += 1
        self.live += 1
        self.peak = max(self.peak, self.live)

    def attempt(self, accepted: bool):
        assert self.live >= 3
        if accepted:
            self.successful += 1
            self.live -= 2
        else:
            self.rejected += 1
            self.live -= 3
        assert self.acquired == 2 * self.successful + 3 * self.rejected + self.live


def simulate_one(level: int, probabilities: list[float], rng: random.Random):
    tracker = RegisterTracker()

    def prepare(depth: int):
        if depth == 0:
            tracker.acquire()
            return
        while True:
            for _ in range(3):
                prepare(depth - 1)
            accepted = rng.random() < probabilities[depth - 1]
            tracker.attempt(accepted)
            if accepted:
                return

    prepare(level)
    assert tracker.live == 1
    assert tracker.peak <= 2 * level + 1
    assert tracker.successful + tracker.rejected <= (tracker.acquired - 1) // 2
    return tracker


def check_asymptotics():
    with localcontext() as context:
        context.prec = 100
        p = Decimal(3) / 5
        mean = Decimal(1)
        scaled_errors, scaled_means = [], []
        q0 = (3 - p) / (3 * (2 * p * p - p + 1))
        for j in range(36):
            scaled_errors.append((1 - p) * Decimal(3) ** j)
            scaled_means.append(mean / (Decimal(6) ** j))
            q = (3 - p) / (3 * (2 * p * p - p + 1))
            assert Decimal(1) / 3 <= q <= q0
            assert p <= visibility_map(p) < 1
            mean *= 3 / success(p)
            p = visibility_map(p)
        assert abs(scaled_errors[-1] / scaled_errors[-6] - 1) < Decimal("1e-12")
        assert abs(scaled_means[-1] / scaled_means[-6] - 1) < Decimal("1e-12")
        return {"scaled_error_limit_approx": float(scaled_errors[-1]),
                "scaled_mean_limit_approx": float(scaled_means[-1]),
                "achieved_exponent": math.log(6) / math.log(3)}


def main():
    finite = design(Fraction(3, 5), Fraction(1, 100), Fraction(1, 20))
    assert finite["levels"] == 5
    assert finite["cap"] == 108011
    assert finite["runs"] == 5
    assert finite["budget"] == 540055
    assert 3 * (1 - finite["visibility"]) / 4 <= Fraction(1, 100)
    assert design(Fraction(3, 5), Fraction(31, 100), Fraction(1, 20))["budget"] == 1
    assert design(Fraction(1), Fraction(1, 100), Fraction(1, 20))["budget"] == 1

    mean2, variance2, probabilities2 = iid_moments(0.6, 2)
    coefficients = second_level_distribution(*probabilities2)
    total = math.fsum(coefficients)
    distribution_mean = math.fsum(3 * n * q for n, q in enumerate(coefficients))
    distribution_variance = math.fsum((3 * n - mean2) ** 2 * q
                                      for n, q in enumerate(coefficients))
    assert abs(total - 1) < 2e-12
    assert abs(distribution_mean / mean2 - 1) < 2e-11
    assert abs(distribution_variance / variance2 - 1) < 2e-10
    for n in [3, 10, 30, 70, 150]:
        positive = positive_second_level_probability(n, *probabilities2)
        assert abs(positive - coefficients[n]) < 2e-13
    cap2 = math.ceil(2 * mean2)
    exact_iid_abort_approx = 1 - math.fsum(coefficients[:cap2 // 3 + 1])
    assert 0 <= exact_iid_abort_approx <= 0.5

    mean3, variance3, probabilities3 = iid_moments(0.6, 3)
    rng = random.Random(20261117)
    samples = [simulate_one(3, probabilities3, rng) for _ in range(300)]
    sampled_mean = math.fsum(x.acquired for x in samples) / len(samples)
    assert abs(sampled_mean - mean3) <= 8 * math.sqrt(variance3 / len(samples))

    summary = {
        "status": "passed",
        "finite_example": {
            "initial_visibility": "3/5", "requested_infidelity": "1/100",
            "failure_allowance": "1/20", "levels": finite["levels"],
            "achieved_infidelity": float(3 * (1 - finite["visibility"]) / 4),
            "exact_mean_as_decimal": float(finite["mean"]),
            "cap_per_run": finite["cap"], "runs": finite["runs"],
            "hard_native_pair_budget": finite["budget"],
            "pair_half_qubits_per_lab": 2 * finite["levels"] + 1,
        },
        "iid_cost_distribution_check": {
            "level": 2, "coefficient_cutoff": len(coefficients) - 1,
            "total_mass": total, "mean_from_distribution": distribution_mean,
            "variance_from_distribution": distribution_variance,
            "cap": cap2, "abort_probability_approx": exact_iid_abort_approx,
        },
        "seeded_register_accounting": {
            "level": 3, "runs": len(samples), "seed": 20261117,
            "maximum_observed_live_pairs": max(x.peak for x in samples),
            "proved_live_pair_bound": 7, "sample_mean_cost": sampled_mean,
            "analytic_mean_cost": mean3,
        },
        "asymptotic_numeric_check": check_asymptotics(),
        "limits": "Finite checks corroborate formulas, not universal proof, priority, or cost optimality.",
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
