# Quantum Blind Entanglement Purification

**Can two separated laboratories purify an entangled pair without learning which maximally entangled state they share?** A fixed three-pair local filter raises a shared fidelity floor even when the input noise strengths and axes differ. It preserves the same unknown physical target.

Each laboratory processes its three qubits with a fixed Schur circuit and measures a chiral multiplicity label. Opposite accepted labels leave one physical output qubit at each laboratory. The gate sequence and acceptance rule use neither the target orientation nor the actual input quality.

For independent inputs about one common unknown target,

```math
\rho_p(U)=p\Phi_U+(1-p)I_4/4,\qquad 1/3\lt p\lt 1,
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
| What if strengths and error axes differ? | For independent pairs with maximally mixed marginals and the same unknown target, the filter raises any common fidelity floor above one half. | [Sharp heterogeneous floor](science/anisotropic-noise.md) |
| How much error can a fixed block remove near purity? | For each $`n\ge3`$, local operations attain the optimal first-order infidelity factor $`1/n`$, even compared with joint operations preserving the clean target. | [Fixed-block limit](science/near-pure-limit.md) |
| Can repeated use have a finite budget? | An explicit cap-and-restart protocol counts every failed attempt and produces one high-fidelity output at specified confidence. | [Resources](science/resources.md) |
| Is there a concrete circuit? | An ancilla-free local three-qubit compiler emits 194 CNOTs and 227 arbitrary one-qubit gates per laboratory, before optimization. | [Implementation](science/implementation.md) |
| How accurate must the apparatus be? | Complete-instrument error bounds control success and accepted fidelity; the required precision tightens near purity. | [Imperfect operations](science/robustness.md) |

At a common input fidelity floor of **0.70**, the three-pair filter guarantees accepted fidelity at least **0.75862** for the heterogeneous source class. Three orthogonal error axes attain that floor. For identical isotropic inputs at fidelity **0.70**, the accepted fidelity is **0.785714** and the success probability is **0.224**. Each attempt consumes all three pairs. The isotropic cap-and-restart example in the [resource account](science/resources.md) uses at most **540,055 native pairs** to reach at least **0.99** fidelity with probability at least **0.95**.

## Read the science

Start with the [scientific reading route](science/README.md). The [protocol](science/protocol.md) gives the physical instrument and proves covariance; the [interpretation](science/interpretation.md) connects the phase choice, target preservation and resource costs. [Related work](references/RELATED_WORK.md) credits the two-copy obstruction, earlier local Schur filters and universal coding, while distinguishing their output promises. [The LLM guide](llms.txt) maps questions to authoritative proofs and checks.

## Learn the project

The [learning route](learning/README.md) connects Nielsen and Chuang's *Quantum Computation and Quantum Information*, 10th anniversary edition (2010), to this construction. Start with the [anchor bridge and worked example](learning/ANCHOR.md), then follow the [30-milestone map](learning/MILESTONES.md). The textbook supplies quantum-information foundations; the project supplies the chiral filters, finite-budget theorem and implementation bounds.

## Reproduce the checks

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
python3 verification/check_learning.py
```

The [verification guide](verification/README.md) explains exact symbolic contractions, full-matrix covariance and circuit checks, resource-distribution checks and noisy-instrument tests. Finite tests support their stated scope; the uniform guarantees follow from the written proofs and the cited two-copy theorem.

## Scope

The heterogeneous theorem assumes maximally mixed marginals and one common fixed target eigenvector. Classical mixtures of product sources need the floor in every component. The first-order comparison uses fixed block size, independent identical inputs with orthogonal noise, and positive clean-input success. The ideal local operations have separate [finite-precision bounds](science/robustness.md).

The three-pair threshold counts specimens. The sharp heterogeneous fidelity is the worst case for this particular instrument. The resource account gives achievable specimen counts, and the gate count applies to the explicit three-pair circuit. A calibrated standard Bell pair can require additional information or processing.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
