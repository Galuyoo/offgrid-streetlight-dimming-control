# Paper configuration notes

The core notebook uses `MODE` to control runtime.

## Modes

- `light`: quick local smoke test.
- `review_fast`: repeated-run manuscript revision configuration.

The `review_fast` mode corresponds to five grouped battery split seeds and two RF model seeds for model-driven policies. Baseline rows are deduplicated by split seed where applicable.