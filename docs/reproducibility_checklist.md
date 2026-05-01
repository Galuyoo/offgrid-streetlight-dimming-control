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

- `light`: quick local smoke test
- `review_fast`: manuscript revision configuration for repeated-run analyses

## Expected generated outputs

The main notebook writes outputs to:

- `outputs/tables/`
- `outputs/figures/`
- `outputs/review_validation/`

Generated outputs are not tracked by default except for placeholder `.gitkeep` files.

## Raw data

The raw NASA battery dataset is not redistributed in this repository. Users can obtain it from the original NASA source or the Kaggle conversion linked in `data/README.md`.
