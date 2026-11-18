"""
Script Mestre (00_master.py): Executa toda a pipeline empírica em sequência.
"""

import subprocess
import sys

SCRIPTS = [
    "src/1_data_collection/01_collect_data.py",
    "src/2_data_treatment/02_clean_and_merge.py",
    "src/3_exploratory_analysis/03_descriptive_stats.py",
    "src/4_econometric_analysis/04_baseline_models.py",
    "src/5_robustness_checks/05_robustness.py",
    "src/6_tables_and_figures/06_plots.py",
]


def main() -> None:
    for script in SCRIPTS:
        print(f"\n==> Executando {script}...")
        result = subprocess.run([sys.executable, script], check=True)
        if result.returncode != 0:
            raise RuntimeError(f"Falha ao executar {script}")
    print("\nPipeline empirica concluida com sucesso!")


if __name__ == "__main__":
    main()
