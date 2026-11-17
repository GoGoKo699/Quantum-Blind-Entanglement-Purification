#!/usr/bin/env python3
"""Reconstruct the three-pair LOCC instrument using exact SymPy arithmetic.

This checks finite-dimensional identities used by the written proof. It is not
a literature-priority check, an experimental validation, or an LOCC optimizer.
Run from the repository root with: python3 verification/check_exact.py
"""
import itertools
import json
import sympy as sp


def zero(matrix):
    return all(sp.simplify(x) == 0 for x in matrix)


def intertwiners():
    a = sp.zeros(2, 8)
    a[0, 2], a[0, 4] = 1 / sp.sqrt(2), -1 / sp.sqrt(2)
    a[1, 3], a[1, 5] = 1 / sp.sqrt(2), -1 / sp.sqrt(2)
    b = sp.zeros(2, 8)
    b[0, 1] = sp.sqrt(sp.Rational(2, 3))
    b[0, 2] = b[0, 4] = -1 / sp.sqrt(6)
    b[1, 6] = -sp.sqrt(sp.Rational(2, 3))
    b[1, 3] = b[1, 5] = 1 / sp.sqrt(6)
    return a, b


def permutation(positions):
    """Return |b> -> |b_positions[0] b_positions[1] b_positions[2]>."""
    result = sp.zeros(8)
    for index in range(8):
        bits = [(index >> i) & 1 for i in (2, 1, 0)]
        output = sum(bits[positions[j]] << (2 - j) for j in range(3))
        result[output, index] = 1
    return result


def grouped_input(pair_states):
    """Reorder A1 B1 A2 B2 A3 B3 to A1 A2 A3 B1 B2 B3."""
    indices = []
    for alice in range(8):
        for bob in range(8):
            original = 0
            for bit in (2, 1, 0):
                original = (original << 2) | (
                    (((alice >> bit) & 1) << 1) | ((bob >> bit) & 1)
                )
            indices.append(original)
    return sp.kronecker_product(*pair_states).extract(indices, indices)


def accepted_output(pair_states, left, right):
    source = grouped_input(pair_states)
    k = sp.kronecker_product(left, right)
    return (k * source * k.conjugate().T).applyfunc(sp.simplify)


def main():
    checks = []

    def require(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    a, b = intertwiners()
    eye2, eye4, eye8 = sp.eye(2), sp.eye(4), sp.eye(8)
    cp, cm = (a + sp.I * b) / sp.sqrt(2), (a - sp.I * b) / sp.sqrt(2)
    phi = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
    target = phi * phi.T
    require("orthogonal real coisometries", zero(a*a.T-eye2)
            and zero(b*b.T-eye2) and zero(a*b.T))
    pplus, pminus = cp.conjugate().T*cp, cm.conjugate().T*cm
    reject = eye8 - pplus - pminus
    require("physical three-sector local instrument", zero(pplus*pplus-pplus)
            and zero(pminus*pminus-pminus) and zero(pplus*pminus)
            and zero(reject*reject-reject)
            and sp.simplify(sp.trace(reject)-4) == 0)

    paulis = [sp.Matrix([[0, 1], [1, 0]]),
              sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.diag(1, -1)]
    for k, sigma in enumerate(paulis):
        collective = sum((sp.kronecker_product(
            *[sigma if i == position else eye2 for i in range(3)])
            for position in range(3)), sp.zeros(8)) / 2
        require(f"exact SU2 generator {k}", zero(a*collective-sigma*a/2)
                and zero(b*collective-sigma*b/2))

    swap12, cycle = permutation((1, 0, 2)), permutation((2, 0, 1))
    omega = (-1 + sp.I*sp.sqrt(3))/2
    require("chiral transposition", zero(cp*swap12+cm)
            and zero(cm*swap12+cp))
    require("chiral three-cycle", zero(cp*cycle-omega*cp)
            and zero(cm*cycle-sp.conjugate(omega)*cm))

    rational = sp.Rational
    qs = [rational(1, 8), rational(1, 8), rational(1, 6), rational(1, 2)]
    ns = [rational(1, 32), rational(1, 24), rational(1, 8), rational(1, 2)]
    for pure_positions in itertools.product((False, True), repeat=3):
        states = [target if pure else eye4/4 for pure in pure_positions]
        first = accepted_output(states, cp, cm)
        second = accepted_output(states, cm, cp)
        count = sum(pure_positions)
        q, n = qs[count], ns[count]
        w = (4*n-q)/3
        expected = w*target+(q-w)*eye4/4
        require(f"exact pure/mixed contraction {pure_positions}",
                zero(first-second) and zero(first+second-expected))

    p1, p2, p3 = sp.symbols("p1 p2 p3", real=True)
    e1, e2, e3 = p1+p2+p3, p1*p2+p1*p3+p2*p3, p1*p2*p3
    q, w = (6*e3+e2+3)/24, (15*e3+6*e2+e1)/72
    states = [p*target+(1-p)*eye4/4 for p in (p1, p2, p3)]
    direct = accepted_output(states, cp, cm)+accepted_output(states, cm, cp)
    require("full unequal-visibility output", zero(direct-w*target-(q-w)*eye4/4))
    g = w/q
    denominator = 6*e3+e2+3
    for index, variable in enumerate((p1, p2, p3)):
        x, y = [v for v in (p1, p2, p3) if v != variable]
        numerator = (3+18*(x+y)+44*x*y-x*x-y*y
                     -6*x*y*(x+y)-21*x*x*y*y)
        require(f"quality-floor derivative {index}", sp.simplify(
            sp.diff(g, variable)-numerator/(3*denominator**2)) == 0)

    p = sp.symbols("p", real=True)
    f = p*(5*p+1)/(3*(2*p*p-p+1))
    success = (p+1)*(2*p*p-p+1)/8
    fidelity = (1+3*f)/4
    require("equal-visibility reduction", sp.simplify(g.subs(
        {p1:p, p2:p, p3:p})-f) == 0)
    require("exact strict gain", sp.simplify(fidelity-(1+3*p)/4
        -p*(1-p)*(3*p-1)/(2*(2*p*p-p+1))) == 0)
    require("fixed points and late-stage contraction", f.subs(p, 0) == 0
            and f.subs(p, rational(1, 3)) == rational(1, 3)
            and f.subs(p, 1) == 1
            and sp.diff(f, p).subs(p, 1) == rational(1, 3))
    require("worked seventy-percent example",
            fidelity.subs(p, rational(3, 5)) == rational(11, 14)
            and success.subs(p, rational(3, 5)) == rational(28, 125))

    # One exact non-real target guards specifically against U -> conjugate(U).
    unitary = sp.Matrix([[rational(3, 5), 4*sp.I/5], [4*sp.I/5, rational(3, 5)]])
    psi_u = sp.kronecker_product(eye2, unitary)*phi
    target_u = psi_u*psi_u.conjugate().T
    visibility = rational(3, 5)
    rotated = visibility*target_u+(1-visibility)*eye4/4
    direct_u = (accepted_output([rotated]*3, cp, cm)
                +accepted_output([rotated]*3, cm, cp))
    expected_u = success.subs(p, visibility)*(f.subs(p, visibility)*target_u
                  +(1-f.subs(p, visibility))*eye4/4)
    require("same non-real unknown target retained", zero(direct_u-expected_u))

    # Complete rank-one family: fix the removable phase so a is real.
    aa, x, y = sp.symbols("a x y", real=True)
    c = aa*a+(x+sp.I*y)*b
    pair = p*target+(1-p)*eye4/4
    output = accepted_output([pair]*3, c, sp.conjugate(c))
    norm = aa*aa+x*x+y*y
    t = 4*aa*aa*y*y
    s_general = norm**2*(1+3*p*p)/16-t*p*p*(1-p)/8
    n_general = norm**2*(1+3*p)*(1+3*p*p)/64-t*p*(1-p)**2/32
    require("complete rank-one success polynomial", sp.simplify(
        sp.trace(output)-s_general) == 0)
    require("complete rank-one overlap polynomial", sp.simplify(
        (phi.T*output*phi)[0]-n_general) == 0)
    t = sp.symbols("t", real=True)
    d = 1+3*p*p-2*t*p*p*(1-p)
    ft = ((1+3*p)*(1+3*p*p)-2*t*p*(1-p)**2)/(4*d)
    require("rank-one gain and strict chirality derivative", sp.simplify(
        ft-(1+3*p)/4-t*p*(1-p)*(p+1)*(3*p-1)/(2*d)) == 0
        and sp.simplify(sp.diff(ft, t)
        -p*(1-p)*(p+1)*(3*p-1)*(1+3*p*p)/(2*d*d)) == 0)

    print(json.dumps({"status": "PASS", "checks": checks,
                      "sympy_version": sp.__version__}, indent=2))


if __name__ == "__main__":
    main()
