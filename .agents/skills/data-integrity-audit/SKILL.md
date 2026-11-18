---
name: data-integrity-audit
description: Forensic audit of data authenticity, deflation, merge integrity, panel structure, lags/leads, and look-ahead bias across data/raw/, src/1_data_collection/, src/2_data_treatment/, and data/processed/. Use before trusting any econometric result or when checking for silent fallbacks/imputations.
---

# Data Integrity Audit

Forensic protocol to guarantee that empirical data is authentic, properly treated, and free of silent fallbacks, merge blow-ups, or panel/lag contamination.

## 6-Step Audit Checklist

1. **Raw Data Authenticity & Anti-Fallback Scan:**
   - Verify `data/raw/` files exist physically, are non-empty, and match expected schemas.
   - Scan `src/` for forbidden silent fallbacks (`try/except` generating `np.random` data, silent `fillna(0)` or `fillna(mean)`).
2. **Deflation, Currency & Scale Consistency:**
   - Verify monetary variables are deflated by an explicit price index (e.g., IPCA, CPI) with base year factor = 1.0.
   - Check unit alignment across merged sources (e.g., thousands vs. units).
3. **Merge Integrity & Sample Attrition:**
   - Verify no unintended many-to-many explosions or silent row drops during joins.
   - Confirm `results/tables/sample_attrition.csv` accounts for every observation from raw to final panel.
4. **Panel Key Uniqueness & Temporal Lags:**
   - Assert zero duplicate `(entity, time)` keys in `data/processed/`.
   - Verify `shift()` / `lag` operations are grouped by entity and respect calendar gaps (no $t-3$ treated as $t-1$, no look-ahead bias).
5. **Winsorization & Outliers:**
   - Confirm winsorization is applied only to intended continuous variables after cleaning and documented in `data/codebook.md`.
6. **Lineage Report Verification:**
   - Confirm `results/logs/data_lineage_report.md` exists and reports `STATUS: PASS`.
