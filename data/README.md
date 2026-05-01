# Data instructions

The NASA battery dataset is not redistributed in this repository.

## Source

Use the NASA Ames Prognostics Center of Excellence battery dataset or the Kaggle community conversion:

https://www.kaggle.com/datasets/patrickfleith/nasa-battery-dataset

## Expected layout

Raw data can be placed under:

`data/raw/`

The main reproduction notebook expects the processed feature table:

`data/processed/engineered_metadata.csv`

This file is generated from the dataset metadata and per-cycle trace files. It contains one row per battery cycle with engineered features used for runtime prediction and downstream dimming-control simulation.

The original exploratory preprocessing notebook is preserved under:

`archive/01_data_exploration_preprocessing_original.ipynb`

The cleaned core reproduction notebook starts from the processed file to keep the main paper pipeline focused and reproducible.
