# Adaptive, Uncertainty-Aware Dimming Control for Off-Grid Solar Lighting

## Overview

This repository presents a **forecast-guided, uncertainty-aware dimming control pipeline** for **off-grid solar-powered street lighting systems**.  
The work addresses a central challenge in autonomous public lighting: **maximising energy savings while avoiding night-time blackouts under uncertain battery conditions**.

The proposed system combines:
- Machine-learning–based **battery runtime forecasting**
- **Conformal uncertainty calibration**
- **Blackout-rate–aware control policies**
- **Realistic actuation constraints** (ramp limits and hysteresis)

The pipeline is designed as a **research demonstrator with direct industrial relevance**, validated under deployment-like, time-aware evaluation protocols.

---

## Motivation

Off-grid solar lighting systems operate under:
- Finite and degrading battery capacity
- Highly variable environmental conditions
- Strict service reliability requirements (blackouts are unacceptable)

Conventional rule-based dimming strategies are either overly conservative or unsafe.  
This work demonstrates how **calibrated uncertainty** can be translated into **safe, adaptive control decisions**, enabling significant energy savings without violating reliability constraints.

---

## Key Contributions

This repository demonstrates:

- **Rolling-window ML forecasting** of battery runtime from per-cycle voltage, current, and temperature features  
- **Uncertainty-aware control** using conformal residual quantiles as safety buffers  
- **Blackout-rate budgeting**, allowing operators to specify acceptable risk levels (e.g. ≤5%)  
- **Multiple control policies**, including:
  - Rule-based baseline
  - Fixed-safety ML controller
  - Block-fixed controller
  - Adaptive safety controller with feedback  
- **Actuation realism**, enforcing brightness ramp limits and hysteresis consistent with commercial lighting drivers  
- **Service-level evaluation**, reporting energy saving, blackout rate, and trade-off curves instead of prediction error alone

---

## Repository Structure

```text
notebooks/
├── 01_data_engineering.ipynb
│   Feature engineering and dataset preparation from battery telemetry
│
├── 02_model_training_rolling.ipynb
│   Rolling-window model training and runtime forecasting
│
└── 03_ktp_pipeline_demo.ipynb
    End-to-end demonstrator:
    forecast → uncertainty calibration → control policies → actuation → KPIs
