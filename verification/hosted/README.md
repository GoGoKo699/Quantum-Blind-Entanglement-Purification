# Hosted mathematical verification

The collector visits the actual public, commit-pinned GitHub pages in a fresh unsigned-in Chromium context. It compares their mathematical structure with the expressions in that exact Git revision, at widths 1440 and 760 pixels, and saves screenshots for visual review. Local source compilation supplies the comparison reference. It is not the hosted observation.

The [text contract](math-contract.json) additionally requires the visible headline map, entangled interval and quality-floor inequalities. It strengthens the full structural comparison without exempting any expression.

The four scripts here are copied unchanged from [Guinevere at revision 39f8043](https://github.com/GoGoKo699/Guinevere/tree/39f8043d14ab5c743e8efe6a328b8a10369698ad/plugins/merlin-arthur-research/skills/merlin-arthur-research/scripts). Their original Git blob identifiers are:

| File | Git blob |
| --- | --- |
| `capture_hosted_math.cjs` | `e8d2c87b345b1c94c11e01b8661f92e4abf8d97d` |
| `probe_hosted_math.cjs` | `f83ea9da799bee0b53bd5c57315ae2b4b2d9de43` |
| `check_rendered_math.py` | `1d3bf9810d0dfadb844a48b354af80f9b66924bc` |
| `check_completion.py` | `d4b9bd29ecefb49998a1859fb4f2443908448be4` |

The [workflow](../../.github/workflows/hosted-math.yml) runs only for a pull request from this repository, checks out its exact head, uses `contents: read`, and does not persist Git credentials. Runtime dependencies and captures live in temporary directories. Playwright 1.56.1 and MathJax 3.2.1 are the pinned, documented collector recipe. The job first probes [the algebra page](../../science/algebra.md), then captures the full Markdown inventory even if the representative comparison reports a defect. Artifacts retain both outcomes and the scientific and navigation check logs for 14 days.

For a permitted local browser environment, install the same runtime outside the checkout and run:

```bash
NODE_PATH=/absolute/temporary/runtime/node_modules node verification/hosted/probe_hosted_math.cjs \
  --root /absolute/scientific-checkout \
  --repository GoGoKo699/Quantum-Blind-Entanglement-Purification \
  --revision FULL_40_CHARACTER_COMMIT \
  --page science/algebra.md \
  --output /absolute/new-empty-probe-directory

NODE_PATH=/absolute/temporary/runtime/node_modules node verification/hosted/capture_hosted_math.cjs \
  --root /absolute/scientific-checkout \
  --repository GoGoKo699/Quantum-Blind-Entanglement-Purification \
  --revision FULL_40_CHARACTER_COMMIT \
  --contract verification/hosted/math-contract.json \
  --output /absolute/new-empty-capture-directory
```

On an exact pinned navigation that returns HTTP 502, 503 or 504, the collector retries once. After a transient interruption, a fresh output directory and `--resume-from` can reuse passing receipts only when the source, scope, contract, helpers, runtime and receipt freshness agree.

A passing probe covers one page only. A passing full structural report still requires actual screenshot inspection against the source; neither establishes scientific correctness. Keep failed reports distinct from later successful captures. The completion checker validates supplied evidence consistency and does not create missing observations.
