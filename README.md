# Off-grid Streetlight Dimming Control

[![Static repository checks](https://github.com/Galuyoo/offgrid-streetlight-dimming-control/actions/workflows/static-checks.yml/badge.svg)](https://github.com/Galuyoo/offgrid-streetlight-dimming-control/actions/workflows/static-checks.yml)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-research%20code-orange)
![Reproducibility](https://img.shields.io/badge/reproducibility-paper%20pipeline-green)
![Dataset](https://img.shields.io/badge/dataset-NASA%20Battery-lightgrey)

This repository contains the reproducibility code and supporting research notebooks for the paper:

**Uncertainty aware Dimming Control for Off grid Solar Street Lighting: Feasibility Bounds and Blackout Severity Metrics**

The repository provides the processed battery-cycle feature table, archived exploratory notebooks, and a cleaned reproduction notebook for the main simulation pipeline. The code covers the core methodological components used in the paper:

- grouped battery-level train/test splitting
- Random Forest runtime forecasting
- residual-quantile uncertainty buffering
- phase-specific dimming policy simulation
- feasibility-bound estimation under brightness floors
- blackout rate, energy saving, and UM|BO severity metrics
- repeated-run confidence-interval analysis
- buffer ablation and severity-percentile sensitivity checks

The main entry point is:

`notebooks/03_reproduce_review_core_results.ipynb`

The archived notebooks in `archive/` preserve the original exploratory preprocessing, model-screening, and full pipeline development history. They are included for traceability, while the cleaned notebook is the recommended reproducibility entry point.

## Repository structure

- `archive/`  
  Original research notebooks preserved for traceability.

- `notebooks/`  
  Cleaned public-facing notebooks:
  - `01_data_exploration_preprocessing.ipynb` - dataset checks and feature engineering
  - `02_model_screening.ipynb` - compact grouped model-screening analysis
  - `03_reproduce_review_core_results.ipynb` - main paper reproduction pipeline

- `data/raw/`  
  Place the downloaded NASA battery dataset here.

- `data/processed/`  
  Place or generate `engineered_metadata.csv` here.

- `outputs/tables/`  
  Generated CSV tables.

- `outputs/figures/`  
  Generated figures.

- `outputs/review_validation/`  
  Supplementary validation outputs.

- `configs/`  
  Reserved for paper configuration files.

## Dataset

The NASA battery dataset is not redistributed in this repository.

Download the dataset from the original source or Kaggle distribution:

- NASA Ames Prognostics Center of Excellence battery dataset
- Kaggle conversion: https://www.kaggle.com/datasets/patrickfleith/nasa-battery-dataset

After preprocessing, the main pipeline expects:

`data/processed/engineered_metadata.csv`

See `data/README.md` for details.

## Installation

Create a Python environment and install the dependencies:

`pip install -r requirements.txt`

## Running the notebooks

The main paper reproduction entry point is:

`notebooks/03_reproduce_review_core_results.ipynb`

The two support notebooks provide preprocessing and model-screening context:

- `notebooks/01_data_exploration_preprocessing.ipynb`
- `notebooks/02_model_screening.ipynb`

The notebook expects:

`data/processed/engineered_metadata.csv`

and writes outputs under:

- `outputs/tables/`
- `outputs/figures/`
- `outputs/review_validation/`

## Notes on reproducibility

Small numerical differences may occur across environments due to package versions and stochastic model training. The notebook uses fixed split and model seeds for the reported repeated-run analyses where applicable.

The archived notebooks are included for traceability but are not intended as the primary reproduction entry point.

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