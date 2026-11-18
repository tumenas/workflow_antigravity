"""
Etapa 6: Geração de Figuras de Publicação (Tables and Figures).
Gera gráfico de tendências paralelas (ROA médio por grupo ao longo do tempo)
e distribuição de ROA em 300 DPI em results/figures/.
"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.utils.helpers import configure_plot_style

PROCESSED_DATA_PATH = os.path.join("data", "processed", "painel_final.csv")
FIGURES_DIR = os.path.join("results", "figures")


def main() -> None:
    if not os.path.exists(PROCESSED_DATA_PATH):
        raise FileNotFoundError(f"Painel final nao encontrado: {PROCESSED_DATA_PATH}")

    df = pd.read_csv(PROCESSED_DATA_PATH)
    os.makedirs(FIGURES_DIR, exist_ok=True)
    configure_plot_style()

    # Gráfico 1: Tendências Paralelas (ROA médio por grupo)
    df["Grupo"] = df["treated"].map({0: "Controle", 1: "Tratado"})
    trend = df.groupby(["year", "Grupo"])["roa_w"].mean().reset_index()

    plt.figure(figsize=(8, 5))
    sns.lineplot(data=trend, x="year", y="roa_w", hue="Grupo", marker="o", linewidth=2.2)
    plt.axvline(x=2019.5, color="gray", linestyle="--", linewidth=1.2, label="Choque Regulatorio (2020)")
    plt.title("Tendencias Paralelas: ROA Medio por Grupo (2016-2023)", fontsize=13, weight="bold", pad=12)
    plt.xlabel("Ano", fontsize=11)
    plt.ylabel("ROA Medio (Winsorizado)", fontsize=11)
    plt.legend(frameon=True)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "tendencias_paralelas_roa.png"), dpi=300, bbox_inches="tight")
    plt.close()

    # Gráfico 2: Distribuição do Q de Tobin por Grupo (Pós-tratamento)
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df[df["post"] == 1], x="Grupo", y="tobin_q_w", palette="Set2")
    plt.title("Distribuicao do Q de Tobin no Periodo Pos-Tratamento", fontsize=13, weight="bold", pad=12)
    plt.xlabel("Grupo", fontsize=11)
    plt.ylabel("Q de Tobin (Winsorizado)", fontsize=11)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "boxplot_tobin_q.png"), dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Figuras salvas em: {FIGURES_DIR}")


if __name__ == "__main__":
    main()
