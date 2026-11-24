# Learning the blind purification result

Imagine a source that repeatedly gives Alice and Bob the same kind of entangled pair. Neither laboratory is told its orientation. Noise makes each specimen imperfect. They want to retain one cleaner specimen of that same unknown state. A procedure that returns a Bell pair chosen by the apparatus would answer a different question.

The entry point is [Nielsen and Chuang, 2010](ANCHOR.md), the single educational anchor. The [30-milestone map](MILESTONES.md) connects the necessary background to the mechanism, proof, implementation and limits of this project. The map records understanding targets and source pointers. It is independent of any reader's progress.

## One complete elementary attempt

A two-qubit pure target is described by a projector $`P_U=|\Phi_U\rangle\langle\Phi_U|`$, where $`|\Phi_U\rangle=(I\otimes U)(|00\rangle+|11\rangle)/\sqrt2`$. The unitary $`U`$ is fixed across the source specimens and is unknown. Each input is

```math
\rho_p(U)=pP_U+(1-p)I_4/4.
```

The visibility $`p`$ specifies how strongly the target contributes relative to completely mixed noise. Target fidelity here is the squared overlap $`F_U(\rho)=\langle\Phi_U|\rho|\Phi_U\rangle`$. It equals $`(1+3p)/4`$ for this source model.

Take three independent inputs with $`p=3/5`$, each of target fidelity $`7/10`$. Alice holds three qubits and Bob holds three. Each applies the same fixed local three-qubit unitary. Each measures two output bits: a sector status and a chirality label. They exchange the records. They retain the last qubit at each laboratory only when both status bits accept and their chirality labels are opposite. No step estimates $`U`$.

The [protocol](../science/protocol.md) gives the unitary's rows as the two chiral maps $`C_\pm=(A\pm iB)/\sqrt2`$, completed by four reject rows. The [exact algebra](../science/algebra.md) gives

```math
f(p)=\frac{p(5p+1)}{3(2p^2-p+1)},\qquad
s(p)=\frac{(p+1)(2p^2-p+1)}8.
```

Here $`f(p)`$ is the accepted output visibility and $`s(p)`$ is the probability of acceptance, summing both opposite-label records.

| Quantity for this attempt | Value | Meaning |
| --- | --- | --- |
| Input visibility | $`3/5`$ | Each input has target fidelity $`7/10`$. |
| Accepted output visibility | $`5/7`$ | The output is isotropic about the same unknown target. |
| Accepted target fidelity | $`11/14\approx0.785714`$ | The conditional improvement is $`3/35\approx0.085714`$. |
| Success probability | $`28/125=0.224`$ | Failure is reported explicitly. |
| Native pairs consumed | Three | Rejected attempts consume all three too. |
| Mean native cost with fresh identical batches until first success | $`3/s=375/28\approx13.393`$ | An expectation; it is not a hard cap. |

This example concerns one accepted pair, with every rejected batch charged. Local calibrated gates and reliable outcome comparison are supplied apparatus resources. The fixed compiler in [implementation](../science/implementation.md) uses 194 CNOTs and 227 arbitrary one-qubit gates per laboratory per attempt, without extra qubit ancillas. Those unoptimized counts do not include a chosen fault-tolerant rotation-synthesis cost.

## Why the operation can preserve something unknown

Three local qubits contain two equivalent spin-half representations. Both carry the unknown rotation in the same way. The extra label distinguishing these representations is called multiplicity. Filtering that label can change the noise without measuring the physical spin qubit that must remain.

Preserving the target is enforced by the exact identity

```math
C_\pm U^{\otimes3}=UC_\pm.
```

It says that rotating all three inputs and then filtering has the same effect as filtering and rotating the retained qubit. The identity is proved for every rotation, rather than inferred from examples of known targets. Covariance alone does not establish purification: the relative imaginary phase between the two multiplicity maps supplies the gain. [Chirality](../science/chirality.md) proves that every real paired rank-one multiplicity filter has zero fidelity gain in this model, whereas the chiral phase maximizes fidelity within that family.

## When the error axes differ

The same circuit improves independent inputs with maximally mixed marginals, the same unknown target as an eigenvector, and individual target fidelities at least $`w\gt1/2`$. Both fidelities and Pauli error axes can differ from pair to pair. Each error component is an orthogonal Bell state obtained by applying a Pauli operator along a real unit axis in the target frame. Pool the two accepted chirality records to obtain one accepted state to which the same input promise applies at a higher floor.

Set $`r=1-w`$. The least accepted fidelity over the promised input class is

```math
W(w)=\frac{3w^3+r^3}{3w^3+r^3+w^2r+3wr^2}\gt w
\qquad (1/2\lt w\lt1).
```

Three rank-two input states of fidelity $`w`$ and mutually orthogonal error axes attain the floor. For $`w=7/10`$, the guaranteed fidelity is $`22/29\approx0.758621`$. The worst-fidelity example succeeds with probability $`29/125`$. The [anisotropic proof](../science/anisotropic-noise.md) relates the accepted overlap and success probability to the dot products between the three axes.

## Near a pure input

For an isotropic input of infidelity $`\epsilon`$, a fixed three-pair attempt has accepted infidelity $`\epsilon/3+O(\epsilon^2)`$. The more general result allows independent copies whose error component is any state orthogonal to the target. Fix a block size $`n`$ and take $`\epsilon`$ to zero. Any success map that preserves every clean target with positive probability has a first-order conditional infidelity coefficient of at least $`1/n`$. Fixed local operations with classical communication attain that coefficient for every $`n\ge3`$. The [near-pure proof](../science/near-pure-limit.md) relates the single-error branches to a small rotation of the unknown clean target. The coefficient concerns output quality conditional on success at each fixed block size.

## From a cleaner pair to a finite preparation procedure

Three completed outputs at one level can feed the next level. For isotropic inputs, the visibility recurrence converges to one whenever the initial visibility exceeds $`1/3`$. For an initial fidelity floor of $`0.70`$, five successful levels guarantee infidelity below $`0.01`$. The explicit conservative construction in [resources](../science/resources.md) caps total consumption at 540,055 native pairs to keep final failure probability at most $`0.05`$, and needs at most eleven pair-half qubits per laboratory. These are ideal-operation guarantees with a supplied quality-floor promise.

For different noise axes, apply the sharp fidelity-floor update at each successful level and use $`w^3/2`$ as a lower bound on its acceptance probability. Pooling the two accepted records preserves the source class for this recurrence. The [resource account](../science/resources.md) gives the corresponding finite budget.

For independent identical isotropic inputs, a schedule of larger blocks after a fixed entry fidelity uses at most $`O(1/\epsilon_{\rm f})`$ native pairs in expectation for target infidelity $`\epsilon_{\rm f}`$. The [block schedule](../science/near-pure-limit.md#expected-specimen-cost-at-fixed-isotropic-input-quality) counts rejected attempts and uses ideal local decoding.

The [robustness account](../science/robustness.md) compares complete instruments, including reject flags, before conditioning on success. It then bounds the entire finite adaptive experiment. An imperfect accepted output need not remain isotropic, so blindly iterating the ideal scalar recurrence would not justify an error guarantee. Fixed positive arbitrary control error also cannot certify unlimited purity.

## Route through the account

Read the [anchor bridge](ANCHOR.md), then follow [M01–M30](MILESTONES.md). For the proof directly, use the [scientific reading route](../science/README.md). The [related-work account](../references/RELATED_WORK.md) separates textbook foundations, inherited research ingredients and this construction. The [verification guide](../verification/README.md) explains what the runnable checks establish.

The output preserves one common unknown target. The source extensions cover the specified isotropic quality mixtures and Pauli-axis noise. The inherited two-copy impossibility and the three-copy construction establish the minimum heralded specimen block. The fixed-block near-pure law identifies the best leading infidelity coefficient. Optimal finite-noise success, minimum coherent memory and hardware advantage remain open.

[Repository overview](../README.md)
