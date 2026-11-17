# Quantum Blind Entanglement Purification

**Can two separated laboratories purify an entangled pair without learning which maximally entangled state they share?** A fixed three-copy local protocol does so throughout the entangled isotropic noise range, preserving the same unknown physical target.

Each laboratory processes its three qubits with a fixed Schur circuit and measures a chiral multiplicity label. Opposite accepted labels leave one physical output qubit at each laboratory. The gate sequence and acceptance rule use neither the target orientation nor the actual input quality.

For independent inputs about one common unknown target,

```math
\rho_p(U)=p\Phi_U+(1-p)I_4/4,\qquad 1/3<p<1,
```

the accepted output is exactly $`\rho_{f(p)}(U)`$, where

```math
f(p)=\frac{p(5p+1)}{3(2p^2-p+1)},\qquad
s(p)=\frac{(p+1)(2p^2-p+1)}8.
```

Here $`s(p)`$ is the success probability per three-pair attempt. Target fidelity means squared overlap, $`F=(1+3p)/4`$.

| Question | Supported result | Account |
|---|---|---|
| How small can a blind purification block be? | Three input pairs suffice. The general two-copy impossibility is inherited from Zhao et al. | [Model and threshold](science/model.md) |
| What supplies the gain? | Conjugate chiral filters maximize fidelity within paired rank-one Schur multiplicity filters; every real filter in that family gives zero gain. | [Chiral phase](science/chirality.md) |
| Must all input qualities be equal? | A pointwise common visibility floor above one third is amplified for product inputs and qualifying classical mixtures. | [Exact algebra](science/algebra.md) |
| Can repeated use have a finite budget? | An explicit cap-and-restart protocol counts every failed attempt and produces one high-fidelity output at specified confidence. | [Resources](science/resources.md) |
| Is there a concrete circuit? | An ancilla-free local three-qubit compiler emits 194 CNOTs and 227 arbitrary one-qubit gates per laboratory, before optimization. | [Implementation](science/implementation.md) |
| How accurate must the apparatus be? | Complete-instrument error bounds control success and accepted fidelity; the required precision tightens near purity. | [Imperfect operations](science/robustness.md) |

For example, input target fidelity **0.70** becomes **0.785714** on acceptance, with probability **0.224** per attempt. All three pairs are consumed whether the attempt succeeds or fails. Recursion has a substantial specimen cost: the conservative construction for output infidelity at most **0.01** and failure probability at most **0.05**, starting from the same 0.70 floor, caps consumption at **540,055 native pairs**.

## Read the science

Start with the [scientific reading route](science/README.md). The [protocol](science/protocol.md) gives the physical instrument and proves covariance; the [interpretation](science/interpretation.md) connects the phase choice, target preservation and resource costs. [Related work](references/RELATED_WORK.md) credits the two-copy obstruction, earlier local Schur filters and universal coding, while distinguishing their output promises. [The LLM guide](llms.txt) maps questions to authoritative proofs and checks.

## Reproduce the checks

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The [verification guide](verification/README.md) explains exact symbolic contractions, full-matrix covariance and circuit checks, resource-distribution checks and noisy-instrument tests. Finite tests support their stated scope; the uniform guarantees follow from the written proofs and the cited two-copy theorem.

## Scope

The exact theorem assumes one common fixed unknown maximally entangled target and isotropic product-source noise. The classical-mixture extension requires a pointwise quality floor in every latent component. Local controls and stored qubits are ideal in that theorem; the separate finite-precision bounds state composable error requirements. The output preserves the unknown target and requires additional processing or information if a calibrated standard Bell pair is desired.

The three-copy threshold concerns input specimens, not minimum coherent memory. The circuit and recursive cost are explicit upper bounds; optimal success, optimal three-copy fidelity, positive asymptotic yield and a hardware advantage are not established.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
