# Physical meaning and use

Imagine that the same source repeatedly distributes a maximally entangled pair to Alice and Bob, but neither party is given a description of its relative orientation. Noise mixes each pair with the completely mixed state. They want a better pair of the same kind, so simply replacing it with a locally chosen standard Bell target would change the requested quantum object.

The three-copy local Hilbert space separates into a spin-three-halves sector and two copies of a spin-half representation. The representation describes how the unknown local orientation acts. The two-fold multiplicity is an extra degree of freedom on which the laboratories can filter while leaving that physical transformation intact. Covariance is the exact statement connecting the input orientation to the output orientation.

The decisive choice is the complex phase between the two spin-half multiplicities. A real rank-one filter retains the target and the original isotropic fidelity. Conjugate chiral filters select opposite orientations of the three-copy cycle, suppressing the noisy contributions relative to the perfect-target contribution. The [exact contraction table](algebra.md) distinguishes batches with zero, one, two and three pure factors; it explains the nonlinear amplification without assuming a known target.

The resulting physical output transforms under the same unknown local unitaries as the original pair. This makes the protocol a target-preserving state processor. In an application where that particular unknown state is the supplied quantum resource, an accepted output can replace a noisier specimen. Turning it into a standard Bell channel in chosen classical frames is a separate task. The construction supplies no target estimate and no free calibration of that channel.

## What three copies establish

The inherited general two-copy no-go and the explicit three-copy filter give a sharp minimum specimen block for the stated blind purification task. The construction raises every common fidelity floor above one half when the pairs have maximally mixed marginals and the same unknown dominant Bell eigenvector. The laboratories can use the same circuit when preparation or storage changes the error axes from pair to pair. The [heterogeneous proof](anisotropic-noise.md) gives the sharp worst case and identifies why the two accepted records must be pooled.

The same conclusion does not require three to be the smallest coherent memory: sequential architectures, work qubits and other models have separate memory questions. The supplied elementary implementation uses three received qubits per laboratory and no extra quantum register. Its 194 CNOTs and 227 arbitrary one-qubit gates are an unoptimized compilation bound. A useful hardware implementation would require its own gate model, timing and observed noise specifications.

## Repetition has a price

Near purity, each successful level reduces infidelity by a factor approaching three, while the elementary success probability approaches one half. Combining three children with retries therefore makes the displayed mean source cost grow by a factor approaching six per level. The achieved single-output cost exponent is consequently $`\log_3 6`$, rather than a claim of positive asymptotic yield. A finite cap and restarts turn this into a fixed-confidence resource guarantee with every rejected batch counted.

The constants worsen near the separability boundary. The [finite example](resources.md#a-numerical-budget-example) counts the resulting specimen cost. Near purity, a [larger cyclic block](near-pure-limit.md) can reduce the first-order error by the full specimen count. The input and heralding costs of that block enter the specimen budget separately.

## Real apparatus errors

The ideal heterogeneous recurrence needs the same Bell eigenvector and maximally mixed marginals. Hardware errors can violate both conditions. Instead, [robustness](robustness.md) compares complete flagged instruments and then the entire finite adaptive experiment before conditioning. This yields a sufficient accuracy requirement for any chosen finite target error. It permits a concrete precision budget without assuming that the accepted state remains isotropic under implementation errors.

A fixed arbitrary control-error allowance cannot guarantee unlimited purity: a final local depolarizing error already creates a nonzero infidelity floor. The method therefore supplies an ideal constructive protocol and explicit finite-precision requirements, with practical yield and hardware performance left to their actual physical models.

[Reading route](README.md) · [Related work](../references/RELATED_WORK.md)
