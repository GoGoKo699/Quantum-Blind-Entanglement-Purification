# The task: improve a pair while preserving its unknown target

Two separated laboratories receive noisy specimens of one fixed maximally entangled two-qubit state. The state is not supplied as a classical description. They want a better specimen of that same state, using local operations and classical communication (LOCC).

## Source and fidelity convention

Fix the computational Bell vector and its locally rotated orbit,

```math
|\Phi\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2},\qquad
|\Phi_U\rangle=(I\otimes U)|\Phi\rangle,\qquad U\in SU(2).
```

Write $P_U=|\Phi_U\rangle\langle\Phi_U|$. Every maximally entangled two-qubit pure state has this form up to an irrelevant global phase. A source specimen with visibility $p$ is

```math
\rho_p(U)=pP_U+(1-p)\frac{I_4}{4},\qquad 0\le p\le1.
```

Throughout, fidelity to a pure target means the squared overlap

```math
F_U(\rho)=\langle\Phi_U|\rho|\Phi_U\rangle,
\qquad F_U(\rho_p(U))=\frac{1+3p}{4}.
```

The state is entangled exactly when $p>1/3$, equivalently $F>1/2$. Indeed, the partial transpose has eigenvalues $(1+p)/4$ with multiplicity three and $(1-3p)/4$ once. Positivity of partial transpose is equivalent to separability in dimension two by two. Thus the interval $1/3\lt p\lt 1$ is the whole noisy entangled isotropic family; it is not a high-fidelity approximation.

## Operations and output

An elementary attempt receives three input pairs. Alice holds $A_1A_2A_3$ and Bob holds $B_1B_2B_3$. Each party may apply a known local circuit, measure local registers, and communicate classical outcome labels. No quantum communication or extra shared entanglement is supplied. On success, one physical qubit remains at each laboratory; the desired output target is still $P_U$.

The circuit and acceptance rule are independent of $U$ and of the input visibilities. Local gate calibration, a consistent ordering of the three specimens, local computational bases and agreed classical outcome labels are part of the apparatus. No estimate of the relative target orientation is needed. The protocol is covariant under independent local unitary changes of basis, as proved in [the protocol account](protocol.md).

Every attempted batch, including rejected batches, is charged three source specimens. The elementary construction simultaneously holds three input qubits per laboratory and uses a fixed local three-qubit unitary and two local readout bits. This is an available implementation, not a lower bound on coherent memory. [Resources](resources.md) counts the complete recursive use.

## Exact constructive statement

For three independent equal-quality inputs, one fixed success map produces

```math
\mathcal E\!\left(\rho_p(U)^{\otimes3}\right)
=s(p)\rho_{f(p)}(U),
```

where

```math
f(p)=\frac{p(5p+1)}{3(2p^2-p+1)},\qquad
s(p)=\frac{(p+1)(2p^2-p+1)}8.
```

It strictly improves target fidelity for every $U$ and every $1/3\lt p\lt 1$. The exact gain is

```math
F_U\!\left(\rho_{f(p)}(U)\right)-F_U\!\left(\rho_p(U)\right)
=\frac{p(1-p)(3p-1)}{2(2p^2-p+1)}.
```

For example, input target fidelity $0.70$ means $p=0.60$. An accepted output has fidelity $11/14\approx0.785714$, with success probability $0.224$ per three-pair attempt. This is a conditional output guarantee with its actual success probability, rather than a deterministic improvement on every attempted batch.

The [exact algebra](algebra.md) proves these formulas, the behavior at every endpoint, and a quality-floor extension. [Chirality](chirality.md) identifies the relative phase that supplies the improvement.

## Why preserving the target is a separate task

Ordinary entanglement distillation often requests a known standard Bell pair. Here the target itself is an unknown quantum object to be preserved. A successful output can replace one source specimen wherever that same target is required; the method does not first estimate, rotate away, or discard its orientation. Its covariance preserves both local transformations of the target.

A purified unknown $P_U$ is not automatically a standard calibrated Bell channel in the parties' chosen computational frames. Transforming it into such a resource can require additional information or processing. Conversely, a protocol that universally outputs a known Bell state does not by itself solve the present same-target purification task. The [related-work account](../references/RELATED_WORK.md) keeps these output promises explicit.

## Three is the minimum heralded specimen block

For any fixed nontrivial depolarizing noise in the entangled range, Zhao et al. prove that a two-to-one LOCC map cannot be nondegrading for every unknown two-qubit maximally entangled target and strictly improving for even one target. See Corollary 4 and supplemental Corollary 7 of [arXiv:2509.08691v2](https://arxiv.org/html/2509.08691v2), published as *Physical Review Letters* **136**, 090203 (2026). Their visibility convention is obtained by setting their global depolarizing parameter to $1-p$; local depolarization has the equivalent isotropic form on this orbit. The no-go theorem allows general LOCC and is inherited here.

Together with the explicit three-input construction, this gives an exact heralded onset of three specimens for strictly improving the complete unknown-target family at each $1/3\lt p\lt 1$. A one-input improvement would give a forbidden two-input map by discarding the second input. The onset concerns the number of noisy source pairs in one elementary block. It does not determine optimal success probability, optimal three-copy fidelity, minimum memory, or the onset for an always-output protocol.

## Quality variation and scope

The exact elementary map also accepts a product of unequal isotropic inputs $\rho_{p_1}(U)\otimes\rho_{p_2}(U)\otimes\rho_{p_3}(U)$. If every visibility satisfies a certified floor $p_i\ge p_0>1/3$, the output has visibility at least $f(p_0)>p_0$. The circuit does not need the values $p_i$. It is not required to outperform the best input. This is why the guarantee does not contradict best-input nondegradation impossibility results.

The [heterogeneous theorem](anisotropic-noise.md) allows different nonisotropic error strengths and axes. It requires that each pair have maximally mixed marginals, with the same target as an eigenvector and a common squared-overlap floor above one half. Pool both accepted signs before using the output. The result allows classical mixtures of product sources with one fixed target and a pointwise floor in every component.

The [fixed-block comparison](near-pure-limit.md) uses independent identical near-pure states and general successful operations that preserve the entire pure input orbit. It optimizes the first-order coefficient at fixed specimen count. The [resource account](resources.md) tracks specimen use and the [robustness account](robustness.md) treats imperfect operations.
