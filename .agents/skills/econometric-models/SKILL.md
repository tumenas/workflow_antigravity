---
name: econometric-models
description: Implement and verify empirical econometric models in src/4_econometric_analysis/ across Python (statsmodels, linearmodels, pyfixest), R (fixest, did, rdrobust), or Stata (reghdfe, ivreghdfe, csdid). Use when estimating Panel FE, Diff-in-Diff, Event Study, IV/2SLS, RDD, or GMM models.
---

# Econometric Models (src/4_econometric_analysis/)

Standardized workflow for estimating baseline and identification models in Economics, Finance, and Management.

## Pre-Flight Check
Before running any model in `src/4_econometric_analysis/`:
1. Confirm `data/processed/painel_final.csv` (or `.parquet`) exists.
2. Confirm `results/logs/data_lineage_report.md` reports `STATUS: PASS`.

## Estimation Standards
- **Panel Fixed Effects:** Always absorb entity and time fixed effects explicitly (`C(firm_id) + C(year)` in `statsmodels`, `PanelOLS` in `linearmodels`, or `feols()` in R `fixest`).
- **Standard Errors:** Cluster standard errors at the unit of treatment assignment or entity level (e.g., firm, municipality, or two-way firm + year).
- **IV / 2SLS:** Always report first-stage F-statistic (Kleibergen-Paap rk Wald F) and test for weak instruments.
- **Outputs:** Save structured coefficient tables to `results/tables/` as `.csv` (for Quarto dynamic import) and `.tex` (for publication), never only to console.
