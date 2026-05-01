# Method overview

This repository implements a reproducible simulation framework for off-grid solar streetlight dimming control under battery-runtime uncertainty.

## Pipeline summary

The workflow has four main stages:

1. Battery discharge feature preparation  
   NASA battery-cycle metadata and per-cycle trace files are converted into an engineered feature table for discharge-runtime prediction.

2. Grouped battery-level forecasting  
   Runtime prediction is evaluated using grouped battery splits so that battery IDs do not appear in both training and test sets.

3. Residual-quantile uncertainty buffering  
   Out-of-fold training residuals are used to construct a conservative residual-quantile buffer. This buffer is applied to predicted runtime before dimming decisions are simulated.

4. Dimming-control simulation  
   Controllers are evaluated under phase-specific minimum brightness floors. The main metrics are:
   - energy saving (ES)
   - blackout rate (BR)
   - unmet minutes conditional on blackout (UM|BO)
   - UM|BO p90 as a tail-severity metric

## Reproducibility scope

The cleaned notebook reproduces the revised core analyses used in the manuscript and reviewer response:

- repeated-run feasibility estimates for Table 3
- Section X confidence-interval tables
- residual-buffer ablation
- UM|BO p75/p90/p95 severity sensitivity

Figures 3--5 in the manuscript are retained as relaxed_oracle diagnostic figures. The cleaned notebook focuses on the additional repeated-run analyses introduced during revision.

## Notes

The raw NASA battery dataset is not redistributed. The processed `engineered_metadata.csv` file is included to make the main simulation pipeline directly runnable.
