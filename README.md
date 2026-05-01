# Off-grid Streetlight Dimming Control

This repository contains the reproducibility code for the paper:

**Uncertainty aware Dimming Control for Off grid Solar Street Lighting: Feasibility Bounds and Blackout Severity Metrics**

The code reproduces the revised core analyses used in the manuscript and reviewer response, including:

- repeated-run feasibility estimates for Table 3
- Section X confidence-interval tables
- residual-buffer ablation
- UM|BO p75/p90/p95 severity sensitivity analysis

Figures 3--5 in the manuscript are retained as relaxed_oracle diagnostic figures. The main reproducibility notebook focuses on the additional repeated-run analyses introduced during revision.

## Repository structure

- `archive/`  
  Original research notebooks preserved for traceability.

- `notebooks/`  
  Contains the cleaned core reproduction notebook:  
  `03_reproduce_review_core_results.ipynb`

- `data/raw/`  
  Place the downloaded NASA battery dataset here.

- `data/processed/`  
  Place or generate `engineered_metadata.csv` here.

- `outputs/tables/`  
  Generated CSV tables.

- `outputs/figures/`  
  Generated figures.

- `outputs/review_validation/`  
  Reviewer-validation outputs.

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

## Running the core reproduction notebook

Open and run:

`notebooks/03_reproduce_review_core_results.ipynb`

The notebook expects:

`data/processed/engineered_metadata.csv`

and writes outputs under:

- `outputs/tables/`
- `outputs/figures/`
- `outputs/review_validation/`

## Notes on reproducibility

Small numerical differences may occur across environments due to package versions and stochastic model training. The notebook uses fixed split and model seeds for the reported repeated-run analyses where applicable.

The archived notebooks are included for traceability but are not intended as the primary reproduction entry point.
