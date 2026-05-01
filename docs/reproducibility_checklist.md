# Reproducibility checklist

## Included

- Cleaned notebook for revised core results:
  - `notebooks/03_reproduce_review_core_results.ipynb`

- Processed metadata table:
  - `data/processed/engineered_metadata.csv`

- Original research notebooks archived for traceability:
  - `archive/01_data_exploration_preprocessing_original.ipynb`
  - `archive/02_model_screening_original.ipynb`
  - `archive/03_pipeline_original.ipynb`

- Dataset instructions:
  - `data/README.md`

- Runtime mode notes:
  - `configs/paper_config_notes.md`

## Runtime modes

The main notebook includes a `MODE` setting with several runtime options:

- `light`: quick smoke test using fewer split/model seeds and a small RF grid.
- `review_fast`: manuscript revision setting used for the repeated-run analyses.
- `medium`: includes optional CatBoost comparison with a moderate runtime.
- `heavy_lite`: larger RF repeated-run setting without CatBoost.
- `heavy`: extended validation setting with more split/model seeds and optional CatBoost.

For a quick check, use:

`MODE = "light"`

For manuscript-level repeated-run reproduction, use:

`MODE = "review_fast"`

## Expected generated outputs

The main notebook writes outputs to:

- `outputs/tables/`
- `outputs/figures/`
- `outputs/review_validation/`

Generated outputs are not tracked by default except for placeholder `.gitkeep` files.

## Raw data

The raw NASA battery dataset is not redistributed in this repository. Users can obtain it from the original NASA source or the Kaggle conversion linked in `data/README.md`.
