# Replication Package README (AEA / DCAS Standard)

## Overview
This replication package reproduces all tables and figures for **[Insert Paper Title]** by **[Authors]**.

## Data Availability Statement
- **Public / Synthetic Data:** Included in `data/raw/` (or describe public source and download date).
- **Restricted / Proprietary Data:** See `access_restricted_data.md` for instructions on how to obtain access (e.g., Economatica, Bloomberg, RAIS, CVM).

## Computational Requirements
- **Software:** Python 3.10+ (packages listed in `requirements.txt`), Quarto CLI (optional, for manuscript rendering).
- **Hardware:** Standard laptop/desktop; estimated runtime < 1 minute.

## Instructions to Replicators
1. Install dependencies: `pip install -r requirements.txt`
2. Run the master script from the project root:
   ```bash
   python src/00_master.py
   ```
   Or on Windows PowerShell:
   ```powershell
   .\run.ps1 analysis
   ```

## Table & Figure Mapping
| Output | Script | Output File |
|---|---|---|
| Table 1 (Descriptive Stats) | `src/3_exploratory_analysis/03_descriptive_stats.py` | `results/tables/tabela_descritiva.csv` |
| Table 2 (Baseline DiD) | `src/4_econometric_analysis/04_baseline_models.py` | `results/tables/coeficientes_baseline.csv` |
| Table 3 (Robustness) | `src/5_robustness_checks/05_robustness.py` | `results/tables/robustez.csv` |
| Figure 1 (Parallel Trends) | `src/6_tables_and_figures/06_plots.py` | `results/figures/tendencias_paralelas_roa.png` |
| Figure 2 (Tobin's Q Boxplot) | `src/6_tables_and_figures/06_plots.py` | `results/figures/boxplot_tobin_q.png` |
