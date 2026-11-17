# A fixed local circuit

The purification instrument has a concrete circuit on the three received
qubits at each laboratory. It needs no extra quantum register. The circuit is
fixed: neither the target orientation nor the input quality changes a gate.
This page gives an explicit compilation into arbitrary one-qubit gates and
CNOTs. It supplies an implementation upper bound, not an optimized circuit or
a fault-tolerant gate estimate.

## Basis and output records

Use the ordered computational basis
$|000\rangle,|001\rangle,\ldots,|111\rangle$, with qubit 0 the most
significant bit. The two real $2\times8$ coisometries are

```math
\begin{aligned}
A_0&=(\langle010|-\langle100|)/\sqrt2,&
A_1&=(\langle011|-\langle101|)/\sqrt2,\\
B_0&=\sqrt{2/3}\langle001|-(\langle010|+\langle100|)/\sqrt6,&
B_1&=-\sqrt{2/3}\langle110|+(\langle011|+\langle101|)/\sqrt6.
\end{aligned}
```

The successful local maps are $C_\pm=(A\pm iB)/\sqrt2$. Define the four
symmetric-sector bras

```math
\begin{aligned}
S_0&=\langle000|,&
S_1&=(\langle001|+\langle010|+\langle100|)/\sqrt3,\\
S_2&=(\langle011|+\langle101|+\langle110|)/\sqrt3,&
S_3&=\langle111|.
\end{aligned}
```

The local unitary is specified by its eight rows:

```math
W=\begin{pmatrix}
(C_+)_0\\(C_+)_1\\(C_-)_0\\(C_-)_1\\
S_0\\S_1\\S_2\\S_3
\end{pmatrix}.
```

Their orthonormality follows from
$AA^\dagger=BB^\dagger=I_2$, $AB^\dagger=0$, and orthogonality of the
spin-half and symmetric spin-three-halves sectors. Thus $W$ is unitary.
Apply $W$, measure output qubits 0 and 1, and keep output qubit 2 when the
local status is successful.

| Measured qubit 0 | Measured qubit 1 | Local operation on the retained qubit |
|---|---|---|
| 0 | 0 | $C_+$; report chirality $+$ |
| 0 | 1 | $C_-$; report chirality $-$ |
| 1 | either | Reject the local block |

The laboratories accept the block when both local statuses are successful and
the chiralities are opposite. No chirality-dependent correction is required.
The two accepted product Kraus operators are $C_+\otimes C_-$ and
$C_-\otimes C_+$. Each attempt uses three input pairs, two measured output
bits per laboratory, and classical comparison of those records. All rejected
inputs are consumed. Ideal classical messages and storage are separate from
the local gate count; their repeated-use costs are treated in
[Resources](resources.md).

## Why the target orientation survives

For $k=x,y,z$, both real maps obey

```math
A\Bigl(\sum_{j=1}^3\sigma_k^{(j)}\Bigr)=\sigma_k A,
\qquad
B\Bigl(\sum_{j=1}^3\sigma_k^{(j)}\Bigr)=\sigma_k B.
```

Exponentiating gives $C_\pm U^{\otimes3}=UC_\pm$ for every $U\in SU(2)$.
This is an exact representation identity, rather than a statement inferred
from sampled rotations. It holds independently at both laboratories.
Consequently a common local rotation of the three inputs becomes the same
rotation of the retained physical output. The parties need an agreed input
ordering and chirality convention, but do not need to learn the target's
orientation or align a shared spatial frame. Their local control and
measurement operations still have to be implemented accurately.

## Explicit elementary-gate compiler

[The compiler](../verification/chiral_circuit.py) uses a deterministic QR
elimination. For two entries $a,b$ in one column, left multiplication on their
two rows by

```math
G(a,b)=\frac1{\sqrt{|a|^2+|b|^2}}
\begin{pmatrix}a^*&b^*\\-b&a\end{pmatrix}\in SU(2)
```

zeros the second entry. The fixed bottom-up elimination of $W$ has fourteen
nontrivial two-level factors and leaves a diagonal phase matrix $D$. If its
chronological left eliminations are $E_1,\ldots,E_{14}$, then
$E_{14}\cdots E_1W=D$. Hence implement $D$ first, followed chronologically
by $E_{14}^\dagger,\ldots,E_1^\dagger$.

The elimination label pairs, in the original decimal basis convention, are

```math
(3,4),(2,3),(1,2),(0,1),(4,5),(3,4),(2,3),
(1,2),(3,4),(2,3),(5,6),(4,5),(3,4),(5,6).
```

The generated diagonal phases, in basis order, are
$0,0,0,0,-5\pi/6,0,5\pi/6,0$. The QR formulas and gate-order rules specify
the circuit independently of the floating-point check.

### A two-level factor uses no ancilla

To act by a known $U\in SU(2)$ on the ordered basis pair $(u,v)$:

1. Apply $X$ gates translating the bit string $u$ to $000$.
2. For the nonzero difference $u\mathbin{\oplus}v$, move one nonzero pivot
   bit to qubit 2 by at most one SWAP, then use qubit 2 as the control of
   CNOTs clearing the other two difference bits. The resulting affine
   permutation $P$ sends $(u,v)$ to $(000,001)$. A SWAP costs three CNOTs;
   this step and its inverse together use at most ten CNOTs and six $X$ gates.
3. Flip both control qubits, perform $U$ on qubit 2 controlled on qubits 0
   and 1 being $11$, restore the control flips, then apply $P^\dagger$.

The doubly controlled operation itself has an explicit reduction. Choose
$V\in SU(2)$ with $V^2=U$. In chronological order, use

```math
\operatorname{C}_{1}(V),\quad
\operatorname{CNOT}_{0\to1},\quad
\operatorname{C}_{1}(V^\dagger),\quad
\operatorname{CNOT}_{0\to1},\quad
\operatorname{C}_{0}(V),
```

where each controlled $V$ targets qubit 2. On classical control bits $a,b$,
the target exponent of $V$ is $b-(b\mathbin{\oplus}a)+a=2ab$, and the
controls are returned unchanged.

Each controlled $V$ reduces to two CNOTs and three one-qubit matrices. Write
$V=R_z(\alpha)R_y(\theta)R_z(\beta)$, and set

```math
\begin{aligned}
A_V&=R_z(\alpha)R_y(\theta/2),\\
B_V&=R_y(-\theta/2)R_z[-(\alpha+\beta)/2],\\
C_V&=R_z[(\beta-\alpha)/2].
\end{aligned}
```

Then $A_VB_VC_V=I$ and $A_VXB_VXC_V=V$. The chronological circuit is
$C_V$, CNOT, $B_V$, CNOT, $A_V$, all three one-qubit matrices acting on the
target. There is no unaccounted controlled phase, because $V\in SU(2)$.
Thus a two-level factor costs at most eighteen CNOTs and nineteen arbitrary
one-qubit gates, including the affine changes and control flips.

### Diagonal phases

For phases $\phi_x$, define their Walsh coefficients

```math
\vartheta_S=\frac18\sum_{x\in\{0,1\}^3}
\phi_x(-1)^{S\cdot x}.
```

Then $D=e^{i\vartheta_\varnothing}\prod_{S\ne\varnothing}
e^{i\vartheta_SZ_S}$. Compute the parity on the last qubit of $S$, apply
$R_z(-2\vartheta_S)$, and uncompute. The seven nonempty subsets use at most
ten CNOTs and seven one-qubit rotations in total. The global phase is recorded
separately and has no effect on the physical instrument.

## Gate and accuracy accounting

The resulting conservative general bound is 262 CNOTs and 273 arbitrary
one-qubit gates per laboratory per attempt. The supplied deterministic
compiler actually emits **194 CNOTs and 227 one-qubit gates**, with zero
ancillas. These are counts of an explicit unoptimized sequence; identity
rotations and cancellations are retained. Both laboratories together use
twice those counts. The generator can export every chronological gate matrix:

```bash
python3 verification/chiral_circuit.py --write /tmp/chiral-circuit.json
python3 verification/check_circuit.py
```

Arbitrary one-qubit gates include non-Clifford rotations. The displayed counts
are therefore not Clifford+T counts. If fault-tolerant synthesis is used, its
rotation precision and resulting cost must be added. The
[robustness account](robustness.md) propagates a per-attempt instrument error
through postselection and repeated use. Finite implementation accuracy cannot
be replaced by the numerical residual of the ideal circuit generator.

The checks reconstruct the full $8\times8$ unitary from the elementary gates,
verify all three collective-spin generator identities, check local instrument
completeness, exercise every one of the 28 possible label pairs in the affine
compiler, and test diagonal phases and square-root branch endpoints. These
finite checks verify the supplied compiler; the gate identities above explain
why its construction is valid.
