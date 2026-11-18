# Reproduce the scientific checks

Use Python 3.11 or newer with the pinned numerical and symbolic dependencies:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
python3 verification/check_learning.py
```

The development run used Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0 and SymPy 1.14.0. The resource check itself uses only the standard library. Each program also runs separately.

| Program | What it checks | Expected outcome |
|---|---|---|
| `check_exact.py` | Symbolic local-instrument identities, all three covariance generators, pure/mixed contraction table, complete unequal-visibility output, monotonicity and general complex paired-filter polynomials | Exact identities pass; reported symbolic residuals vanish. |
| `check_circuit.py` | The chronological one-qubit/CNOT compiler reconstructs the full local unitary; arbitrary label-pair, controlled-gate, diagonal-phase and branch endpoint tests | Numerical residuals below the explicit tolerances; deterministic emitted counts 194 CNOTs and 227 one-qubit gates per laboratory. |
| `check_resources.py` | Exact rational finite budgets, independently reconstructed two-level cost distribution, asymptotic normalized sequences and seeded live-register accounting | All probability, mean, cap and pathwise-accounting checks pass; the worked budget is reproduced. |
| `check_robustness.py` | Full six-qubit noisy maps and the success/conditional-fidelity inequalities, source perturbations and the final-noise counterexample | Every tested bound holds within the numerical tolerance. |
| `check_learning.py` | Exactly M01–M30, the settled phase allocation, six fields per milestone, earlier dependencies, local Markdown targets and entrypoint learning routes | Map and navigation checks pass. Conceptual accuracy is assessed by reading the sources, not inferred from this check. |

The scripts distinguish exact algebra from finite tests. The uniform quality-floor and conditional-history resource theorems follow from their written arguments in [algebra](../science/algebra.md) and [resources](../science/resources.md). Complete-instrument and adaptive-channel inequalities are proved in [robustness](../science/robustness.md). The general two-copy impossibility is imported from the cited primary paper rather than re-proved by enumeration.

## Export the circuit

```bash
python3 verification/chiral_circuit.py --write /tmp/chiral-circuit.json
```

The output lists gates in chronological order, complex one-qubit matrices and a separate global phase. Qubit 0 is most significant. The file is a reproducible numerical representation of the exact compiler identities, not a measured hardware calibration. Arbitrary one-qubit rotations require their actual synthesis precision in a discrete gate library.

## Verification boundary

Finite residuals do not establish optimal LOCC fidelity, maximum success probability, circuit optimality, hardware performance, or an unrestricted-noise theorem. Source checks also do not establish mathematical rendering on the host; hosted review is recorded separately for the integrated furnished revision.
