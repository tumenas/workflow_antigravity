---
name: robustness-checks
description: Design and execute a comprehensive battery of robustness checks in src/5_robustness_checks/ for Economics, Finance, and Management papers. Use when preparing sensitivity analyses, placebo tests, Oster (2019) bounds, alternative proxies, or referee-requested checks.
---

# Robustness Checks (src/5_robustness_checks/)

Structured suite of sensitivity and falsification tests to validate the baseline identification strategy.

## Core Robustness Battery
1. **Placebo / Falsification Tests:**
   - Temporal placebo (assigning a fake shock in the pre-treatment period).
   - Group placebo (untreated industry/region).
2. **Alternative Dependent & Independent Variables:**
   - e.g., ROA vs. ROE vs. Tobin's Q; alternative leverage or size definitions.
3. **Sample & Outlier Sensitivity:**
   - Varying winsorization thresholds (e.g., 1%/99% vs. 2.5%/97.5% vs. raw).
   - Excluding crisis years (e.g., 2008–2009, 2020–2021) or balanced vs. unbalanced panel.
4. **Alternative Clustering & Fixed Effects:**
   - One-way (firm) vs. two-way (firm + year) vs. industry-year FE.
5. **Omitted Variable Bias (Oster 2019):**
   - Compute $\delta$ (degree of selection on unobservables relative to observables) and $\beta^*$ under $R_{\max} = 1.3 \tilde{R}$.

## Output
Save all robustness results in `results/tables/robustez.csv` (and `.tex` if included in `manuscript/online_appendix.qmd`).
