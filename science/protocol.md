# The local chiral filter

The method resolves the two equivalent spin-half representations inside three qubits. It measures a complex superposition of their multiplicity labels while retaining the spin qubit. The same fixed operation works at both laboratories.

## Two explicit intertwiners

Use computational order $000,001,\ldots,111$. Define two maps $A,B:\mathbb C^8\to\mathbb C^2$ by their rows:

```math
\begin{aligned}
A_0&=\frac{\langle010|-\langle100|}{\sqrt2},&
A_1&=\frac{\langle011|-\langle101|}{\sqrt2},\\
B_0&=\sqrt{\frac23}\langle001|
-\frac{\langle010|+\langle100|}{\sqrt6},&
B_1&=-\sqrt{\frac23}\langle110|
+\frac{\langle011|+\langle101|}{\sqrt6}.
\end{aligned}
```

Here $A=|0\rangle A_0+|1\rangle A_1$, and similarly for $B$. Their four rows are orthonormal, so

```math
AA^\dagger=BB^\dagger=I_2,\qquad AB^\dagger=BA^\dagger=0.
```

The ranges of $A^\dagger$ and $B^\dagger$ are the two spin-half copies in

```math
(\mathbb C^2)^{\otimes3}\cong
\mathbb C^4_{j=3/2}\oplus
\left(\mathbb C^2_{\rm multiplicity}\otimes\mathbb C^2_{j=1/2}\right).
```

The spin decomposition and real Clebsch–Gordan maps are standard ingredients. In particular, the local three-qubit Schur-filter architecture is close to Eqs. (21)–(25) of Ahmad et al., [*Distillation of supersinglet states*, arXiv:2509.20962v3](https://arxiv.org/html/2509.20962v3). The useful phase choice here is analyzed in [chirality](chirality.md).

## Local instrument and acceptance rule

Set

```math
C_+=\frac{A+iB}{\sqrt2},\qquad
C_-=\frac{A-iB}{\sqrt2}.
```

These are coisometries with orthogonal input supports:

```math
C_sC_s^\dagger=I_2,\qquad C_+C_-^\dagger=0.
```

Thus $P_s=C_s^\dagger C_s$ are orthogonal rank-two projectors. Their sum is the spin-half projector, and $P_{3/2}=I_8-P_+-P_-$ is a positive rank-four reject projector. Measuring these three orthogonal sectors and decoding the accepted spin-half sector realizes an ordinary trace-nonincreasing local quantum instrument. Rejecting all spin-three-halves outcomes completes it to a trace-preserving instrument when the classical reject flag is included.

Alice and Bob each apply this instrument and report $+$, $-$ or reject. Keep a pair precisely for $(+,-)$ or $(-,+)$. After reordering tensor factors into $A_1A_2A_3:B_1B_2B_3$, the accepted map is

```math
\mathcal E(X)=K_+XK_+^\dagger+K_-XK_-^\dagger,
\qquad
K_+=C_+\otimes C_-,\quad K_-=C_-\otimes C_+.
```

The tensor reordering is notation, not a remote physical gate. Every operation in the construction is local, followed by a comparison of classical records. Successful output qubits are already the physical spin-half outputs; there is no target-dependent correction.

For the source model, the two accepted records have equal probabilities and the same normalized output. The announced success probability is the sum of both probabilities. Keeping only one accepted record would halve success without changing its conditional target fidelity.

## Exact covariance

Let

```math
J_k=\frac12\left(\sigma_k\otimes I\otimes I+
I\otimes\sigma_k\otimes I+I\otimes I\otimes\sigma_k\right).
```

Substitution of the rows above gives

```math
AJ_k=\frac{\sigma_k}{2}A,\qquad
BJ_k=\frac{\sigma_k}{2}B\qquad (k=x,y,z).
```

For a short hand check, both row-zero bras have total $J_z=+1/2$ and both row-one bras have total $J_z=-1/2$. The collective raising operator maps the row-one spin-half state to the row-zero state with coefficient one; the lowering relation is its adjoint. These three generator identities exponentiate to

```math
C_sU^{\otimes3}=UC_s\qquad (U\in SU(2)).
```

Consequently the full accepted map is covariant under independent local rotations:

```math
\begin{aligned}
&\mathcal E\!\left[
(V^{\otimes3}\otimes W^{\otimes3})X
(V^{\dagger\otimes3}\otimes W^{\dagger\otimes3})\right]\\
&\hspace{2em}=(V\otimes W)\mathcal E(X)(V\otimes W)^\dagger.
\end{aligned}
```

The identity holds for each accepted record separately. It transports a result for the canonical target $P=|\Phi\rangle\langle\Phi|$ to every $P_U$ with exactly the same success probability. In particular, the target is not conjugated, transposed, or converted to a basis chosen by the apparatus.

For canonical isotropic inputs, invariance under $V\otimes\overline V$ forces the output to be a linear combination of $P$ and $I_4-P$. The representation on the latter three-dimensional space is irreducible. Therefore success and the target-overlap numerator determine the complete output, not merely its fidelity. [The algebraic calculation](algebra.md) supplies those two scalars.

## Permuting the specimens

Let $T_{12}$ swap the first two local inputs, and let $R$ cyclically permute them by $|b_1b_2b_3\rangle\mapsto|b_3b_1b_2\rangle$. The explicit rows give

```math
AT_{12}=-A,\quad BT_{12}=B,\qquad
AR=-\tfrac12 A-\tfrac{\sqrt3}{2}B,\quad
BR=\tfrac{\sqrt3}{2}A-\tfrac12 B.
```

Writing $\omega=e^{2\pi i/3}$, these imply

```math
C_+T_{12}=-C_-,\quad C_-T_{12}=-C_+,
\qquad C_+R=\omega C_+,\quad C_-R=\overline\omega C_-.
```

The paired accepted map is invariant under simultaneous permutations of the three source pairs: a transposition exchanges its two Kraus operators, and a cycle contributes phases that cancel between the laboratories. This justifies the symmetric-polynomial calculation for unequal qualities in [the exact algebra](algebra.md).

## Finite implementation

Complete the four rows of $C_+,C_-$ with the normalized symmetric rows $\langle000|$, $(\langle001|+\langle010|+\langle100|)/\sqrt3$, $(\langle011|+\langle101|+\langle110|)/\sqrt3$, and $\langle111|$. The resulting known $8\times8$ unitary implements the local instrument with two measured output bits and one retained qubit. [Implementation](implementation.md) fixes its ordering and synthesis. The non-Clifford Clebsch–Gordan angles are physical resources; this is not a stabilizer-only protocol.
