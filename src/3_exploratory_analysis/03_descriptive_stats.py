"""
Etapa 3: Análise Exploratória de Dados (Exploratory Data Analysis).
Gera a Tabela 1 (Estatísticas Descritivas) e Matriz de Correlação em results/tables/.
"""

import os
import pandas as pd

PROCESSED_DATA_PATH = os.path.join("data", "processed", "painel_final.csv")
TABLES_DIR = os.path.join("results", "tables")


def main() -> None:
    if not os.path.exists(PROCESSED_DATA_PATH):
        raise FileNotFoundError(f"Painel final nao encontrado: {PROCESSED_DATA_PATH}")

    df = pd.read_csv(PROCESSED_DATA_PATH)
    os.makedirs(TABLES_DIR, exist_ok=True)

    vars_interesse = ["roa_w", "tobin_q_w", "size_w", "leverage_w"]

    # Tabela 1: Estatísticas descritivas gerais
    desc = df[vars_interesse].agg(["count", "mean", "std", "min", "median", "max"]).T.round(4)
    desc.index.name = "Variavel"
    desc_path = os.path.join(TABLES_DIR, "tabela_descritiva.csv")
    desc.to_csv(desc_path)

    # Matriz de correlação
    corr = df[vars_interesse].corr().round(4)
    corr_path = os.path.join(TABLES_DIR, "matriz_correlacao.csv")
    corr.to_csv(corr_path)

    print(f"Estatistica descritiva salva em: {desc_path}")
    print(f"Matriz de correlacao salva em: {corr_path}")


if __name__ == "__main__":
    main()
