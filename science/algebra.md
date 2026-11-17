# Exact output and quality-floor amplification

The proof uses the explicit local maps in [the protocol](protocol.md). Covariance reduces an arbitrary common target to $P=|\Phi\rangle\langle\Phi|$. It also forces each accepted output to be isotropic, so two traces determine the whole output operator.

## Multilinear calculation

For $J\subseteq\{1,2,3\}$, let $T_J$ be the product input with $P$ on pairs in $J$ and $I_4/4$ on all remaining pairs. Put

```math
q_J=\operatorname{Tr}\mathcal E(T_J),\qquad
n_J=\operatorname{Tr}\!\left[P\mathcal E(T_J)\right].
```

Simultaneous specimen-permutation invariance makes both values depend only on $k=|J|$. Substituting the four rows of $C_\pm$ gives the following rational table. Both accepted records are included.

| Number $k$ of pure factors | $q_k$ | $n_k$ | Conditional target overlap $n_k/q_k$ |
| --- | --- | --- | --- |
| 0 | $1/8$ | $1/32$ | $1/4$ |
| 1 | $1/8$ | $1/24$ | $1/3$ |
| 2 | $1/6$ | $1/8$ | $3/4$ |
| 3 | $1/2$ | $1/2$ | $1$ |

For clarity, this table is a finite contraction identity rather than a numerical inference. With $L_s=C_s\otimes C_{-s}$ and $|\Phi\rangle=\sum_b|bb\rangle/\sqrt2$, its entries are obtained from

```math
q_J=\sum_{s=\pm}\operatorname{Tr}(L_sT_JL_s^\dagger),
\qquad
n_J=\sum_{s=\pm}\langle\Phi|L_sT_JL_s^\dagger|\Phi\rangle.
```

For $k=0$, $T_\varnothing=I_{64}/64$, $L_sL_s^\dagger=I_4$ and the two entries are immediately $8/64$ and $2/64$. For $k=3$, contraction of the three Bell vectors gives

```math
(C_+\otimes C_-)|\Phi\rangle^{\otimes3}
=\tfrac12|\Phi\rangle,
```

and the same identity holds for the opposite record. For $k=1,2$, expanding the remaining maximally mixed factors in computational basis gives the displayed $1/8,1/24$ and $1/6,1/8$. The exact symbolic verifier [check_exact.py](../verification/check_exact.py) carries out these contractions as radical-valued matrices and compares every output entry, including all choices of $J$.

Write the elementary symmetric polynomials of the three input visibilities as

```math
e_1=p_1+p_2+p_3,\qquad
e_2=p_1p_2+p_1p_3+p_2p_3,\qquad
e_3=p_1p_2p_3.
```

Expansion of

```math
\bigotimes_{i=1}^3\bigl[p_iP+(1-p_i)I_4/4\bigr]
=\sum_J\prod_{i\in J}p_i\prod_{i\notin J}(1-p_i)\,T_J
```

and the table give

```math
q=\frac{6e_3+e_2+3}{24},\qquad
n=\frac{21e_3+7e_2+e_1+3}{96}.
```

If $w=(4n-q)/3$, isotropy gives the complete unnormalized output

```math
\mathcal E\!\left(\bigotimes_i\rho_{p_i}(I)\right)
=wP+\frac{q-w}{4}I_4,
\qquad
w=\frac{15e_3+6e_2+e_1}{72}.
```

An alternative entrywise certificate is

```math
\frac1{288}
\begin{pmatrix}
33e_3+9e_2+e_1+9&0&0&2(15e_3+6e_2+e_1)\\
0&3e_3-3e_2-e_1+9&0&0\\
0&0&3e_3-3e_2-e_1+9&0\\
2(15e_3+6e_2+e_1)&0&0&33e_3+9e_2+e_1+9
\end{pmatrix}.
```

Thus, for every $0\le p_i\le1$, the success probability and normalized visibility are exactly

```math
s(p_1,p_2,p_3)=\frac{6e_3+e_2+3}{24},\qquad
g(p_1,p_2,p_3)=\frac{15e_3+6e_2+e_1}{3(6e_3+e_2+3)}.
```

The denominator is at least $9$, so normalization is always well defined. Independent local covariance transports this full operator identity to every unknown common $P_U$.

## Equal visibilities and the entangled interval

For $p_1=p_2=p_3=p$, cancellation of the factor $p+1$ gives

```math
g(p,p,p)=f(p)=\frac{p(5p+1)}{3(2p^2-p+1)},\qquad
s(p,p,p)=\frac{2p^3+p^2+1}{8}
=\frac{(p+1)(2p^2-p+1)}8.
```

The conditional target fidelity is

```math
F_{\rm out}(p)=\frac{1+3f(p)}4
=\frac{7p^2+1}{4(2p^2-p+1)}.
```

Since $2p^2-p+1\ge7/8$, its difference from the input value has the sign of $p(1-p)(3p-1)$:

```math
F_{\rm out}(p)-\frac{1+3p}4
=\frac{p(1-p)(3p-1)}{2(2p^2-p+1)}.
```

This proves strict purification at every $1/3<p<1$. The endpoints and the remaining visibility range are explicit:

| Input visibility | Output visibility | Success | Interpretation |
| --- | --- | --- | --- |
| $p=0$ | $0$ | $1/8$ | Completely mixed input remains completely mixed. |
| $0<p<1/3$ | $f(p)<p$ | Positive | This particular filter does not improve the separable interior. |
| $p=1/3$ | $1/3$ | $4/27$ | The separable boundary is fixed. |
| $1/3<p<1$ | $p<f(p)<1$ | Positive | Strict improvement across the entire noisy entangled family. |
| $p=1$ | $1$ | $1/2$ | The pure unknown target is preserved. |

For $1/3<p<1$,

```math
1-f(p)=\frac{(1-p)(3-p)}{3(2p^2-p+1)}.
```

The sequence $p_{j+1}=f(p_j)$ is increasing and bounded by one. Its limit must solve $f(p)=p$; the only fixed points on $[1/3,1]$ are $1/3$ and $1$. Hence every start $p_0>1/3$ converges to the same unknown pure target. The local derivative $f'(1)=1/3$ sets the late-stage contraction. This convergence statement is conditional on successful recursive preparation; all failures and finite stopping budgets are counted in [resources](resources.md).

## Amplifying an unknown quality floor

The stronger unequal-quality statement follows from coordinatewise monotonicity, not from replacing all three inputs by their average. Put $a=p_2$, $b=p_3$ and $D=6e_3+e_2+3$. Differentiating the exact rational function gives

```math
\frac{\partial g}{\partial p_1}
=\frac{M(a,b)}{3D^2},
```

where

```math
M(a,b)=3+18(a+b)+44ab-a^2-b^2
-6ab(a+b)-21a^2b^2.
```

For $a,b\in[0,1]$, use $a^2\le a$, $b^2\le b$, $a+b\le2$ and $a^2b^2\le ab$ to obtain

```math
M(a,b)\ge3+17(a+b)+11ab>0.
```

Symmetry proves positivity of all three partial derivatives. Therefore

```math
p_i\ge p_0>1/3\quad\Longrightarrow\quad
g(p_1,p_2,p_3)\ge f(p_0)>p_0.
```

The success probability is coordinatewise increasing as well, because $6e_3+e_2+3$ has nonnegative coefficients. It is consequently at least $s(p_0)$ on the promised cube.

The guarantee compares output to a common certified lower floor. A batch with one excellent input and two weaker ones can give an output worse than that excellent input. No best-input nondegradation guarantee is being asserted.

## Classical mixtures and the boundary of the extension

Consider a global product-source mixture

```math
\Omega=\int \mu(d\lambda)\,
\bigotimes_i\rho_{p_i(\lambda)}(U),
\qquad p_i(\lambda)\ge p_0>1/3.
```

Here $U$ is common to every specimen and every mixture component; the quality parameters may have arbitrary classical dependence. For a processed batch, each component's accepted output is isotropic about $P_U$ with visibility at least $f(p_0)$. Success changes the component weights by Bayes reweighting, but cannot lower that pointwise floor. Disjoint successful batches retain the conditional product-mixture form. By induction, grouping three outputs at the same successful depth gives the same floor-amplification rule at later depths, even after conditioning on earlier records.

This argument requires the pointwise product decomposition and its floor. Individual marginal fidelities alone do not provide it. General entangled noise across specimens or varying unknown targets can invalidate both the exact map and the induction. Such inputs have not been promoted into the theorem.
