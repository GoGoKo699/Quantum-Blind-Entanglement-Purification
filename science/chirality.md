# Why the relative phase matters

The spin-half Schur space has two copies of the same physical representation. A real projection onto one multiplicity direction retains the unknown target but supplies no isotropic fidelity gain. A complex relative phase turns that otherwise neutral projection into a purifier.

## The full paired rank-one filter family

Use the real intertwiners $A,B$ from [the protocol](protocol.md). Every normalized rank-one multiplicity filter has the form

```math
C=aA+bB,\qquad |a|^2+|b|^2=1.
```

Consider the accepted product branch $C\otimes\overline C$. It is a valid LOCC branch: $CC^\dagger=I_2$, and its effect is a rank-two projector. The conjugate pairing preserves the pure canonical target. An overall phase of $C$ changes neither its local effect nor the paired branch, so one may take $a$ real and nonnegative when calculating; the case $a=0$ follows by continuity.

Define the multiplicity chirality parameter

```math
t=4\bigl[\mathrm{Im}(\overline a b)\bigr]^2,
\qquad 0\le t\le1.
```

The upper bound follows from $4|a|^2|b|^2\le(|a|^2+|b|^2)^2=1$. It is attained exactly when the two coefficients have equal moduli and relative phase $\pm\pi/2$, up to a common phase.

For three equal-quality inputs, covariance again fixes an isotropic output. The exact single-branch success and target-overlap numerator are

```math
S_t=\frac{1+3p^2-2tp^2(1-p)}{16},
```

```math
N_t=\frac{(1+3p)(1+3p^2)-2tp(1-p)^2}{64}.
```

One way to verify that only $t$ enters is to write $a\in\mathbb R$ and $b=x+iy$. Direct contraction of the three-copy input gives, before normalizing $a^2+x^2+y^2=1$,

```math
\begin{aligned}
16S&=(a^2+x^2+y^2)^2(1+3p^2)
-8a^2y^2p^2(1-p),\\
64N&=(a^2+x^2+y^2)^2(1+3p)(1+3p^2)
-8a^2y^2p(1-p)^2.
\end{aligned}
```

These polynomial identities can be checked by expanding the two local rows; [the exact verifier](../verification/check_exact.py) checks them symbolically without sampling filter coefficients. They cover every complex pair $(a,b)$ because of the removable overall phase.

## Fidelity gain and optimization

The conditional target fidelity is

```math
F_t(p)=\frac{(1+3p)(1+3p^2)-2tp(1-p)^2}
{4[1+3p^2-2tp^2(1-p)]}.
```

Its gain over the input is

```math
F_t(p)-\frac{1+3p}{4}
=\frac{tp(1-p)(p+1)(3p-1)}
{2[1+3p^2-2tp^2(1-p)]}.
```

The denominator is strictly positive on $0\le p,t\le1$, since it is at least $1+3p^2-2p^2(1-p)=1+p^2+2p^3\ge1$. For an entangled noisy input, differentiation yields

```math
\frac{\partial F_t(p)}{\partial t}
=\frac{p(1-p)(p+1)(3p-1)(1+3p^2)}
{2[1+3p^2-2tp^2(1-p)]^2}>0,
\qquad 1/3\lt p\lt 1.
```

Thus the chiral values $t=1$ maximize target fidelity throughout this entire paired rank-one multiplicity-filter family. All real filters have $t=0$ and preserve the input fidelity exactly. This includes real rotations of the standard multiplicity basis, not just the individual filters $A$ and $B$.

The maximizing pair can be chosen as $C_+=(A+iB)/\sqrt2$ and its orthogonal partner $C_-=(A-iB)/\sqrt2$. Both conjugately paired outcomes can then be accepted, doubling $S_1$ without changing the normalized output. Factoring

```math
1+p^2+2p^3=(p+1)(2p^2-p+1)
```

recovers the success and fidelity formulas in [the exact algebra](algebra.md).

## Physical meaning and comparison boundary

The two chiral filters are eigenmaps of the three-cycle on the input copies with eigenvalues $e^{\pm2\pi i/3}$. Their imaginary relative phase resolves opposite cyclic orientations inside the multiplicity space while leaving the physical spin representation intact. The protocol removes noise by this multiplicity filtering and preserves the source's unknown local transformations in the remaining spin qubits.

The local Schur architecture and representation-theoretic covariance are inherited ingredients. Ahmad et al.'s [supersinglet protocol](https://arxiv.org/html/2509.20962v3) uses a closely related real multiplicity filter. Substituting any such real paired filter in the present isotropic two-party task gives $t=0$ and exactly zero target-fidelity gain. The complex phase choice is therefore a consequential change of operation in this model, rather than a new name for a generic Schur projection.

Cross-copy spin chirality also has an established entanglement-detection role: Tulewicz, Bartkiewicz and Nori's [moment-correction analysis](https://arxiv.org/html/2605.14515v1) uses scalar chirality correlators and controlled-SWAP readout. The present addition is a retained quantum-output purification instrument and its guarantee, rather than the introduction of that observable. See [related work](../references/RELATED_WORK.md).

The optimization above fixes one paired rank-one Schur branch. It does not optimize over general LOCC, arbitrary multiplicity instruments, all classical combinations of accepted records, or multi-round three-copy protocols. Neither the achieved fidelity nor the success probability is claimed globally optimal. The separate exact specimen threshold uses the earlier general two-copy no-go theorem together with the present constructive three-copy filter.
