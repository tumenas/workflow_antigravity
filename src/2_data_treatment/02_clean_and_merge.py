"""
Etapa 2: Tratamento de Dados (Data Treatment).
Lê data/raw/firmas_brutas.csv, aplica limpeza, winsorização (1%/99%)
e gera o painel analítico final em data/processed/painel_final.csv.
"""

import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.utils.helpers import winsorize_series

RAW_DATA_PATH = os.path.join("data", "raw", "firmas_brutas.csv")
INTERMEDIATE_PATH = os.path.join("data", "intermediate", "firmas_limpas.csv")
PROCESSED_DATA_PATH = os.path.join("data", "processed", "painel_final.csv")


def main() -> None:
    if not os.path.exists(RAW_DATA_PATH):
        raise FileNotFoundError(f"Arquivo bruto nao encontrado: {RAW_DATA_PATH}")

    df = pd.read_csv(RAW_DATA_PATH)
    df_clean = df.dropna().copy()

    os.makedirs(os.path.dirname(INTERMEDIATE_PATH), exist_ok=True)
    df_clean.to_csv(INTERMEDIATE_PATH, index=False)

    # Winsorizar variáveis contínuas a 1% e 99%
    for col in ["roa", "tobin_q", "size", "leverage"]:
        df_clean[f"{col}_w"] = winsorize_series(df_clean[col], 0.01, 0.99)

    # Criar termo de interação Diff-in-Diff
    df_clean["did"] = df_clean["treated"] * df_clean["post"]

    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    df_clean.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"Painel final salvo em {PROCESSED_DATA_PATH} ({len(df_clean)} obs).")


if __name__ == "__main__":
    main()
