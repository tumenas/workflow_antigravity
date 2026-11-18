"""
Etapa 2: Tratamento de Dados (Data Treatment).
Lê data/raw/firmas_brutas.csv, valida integridade, aplica limpeza,
winsorização (1%/99%) e gera data/processed/painel_final.csv.
"""

import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.utils.helpers import winsorize_series
from src.utils.data_assertions import (
    assert_raw_authentic,
    assert_panel_structure,
    write_lineage_and_attrition,
)

RAW_DATA_PATH = os.path.join("data", "raw", "firmas_brutas.csv")
INTERMEDIATE_PATH = os.path.join("data", "intermediate", "firmas_limpas.csv")
PROCESSED_DATA_PATH = os.path.join("data", "processed", "painel_final.csv")


def main() -> None:
    required_cols = ["firm_id", "year", "sector", "treated", "post", "roa", "tobin_q", "size", "leverage"]
    raw_hash = assert_raw_authentic(RAW_DATA_PATH, required_cols)

    df = pd.read_csv(RAW_DATA_PATH)
    n_raw = len(df)

    df_clean = df.dropna().copy()
    n_dropna = len(df_clean)

    os.makedirs(os.path.dirname(INTERMEDIATE_PATH), exist_ok=True)
    df_clean.to_csv(INTERMEDIATE_PATH, index=False)

    # Winsorizar variáveis contínuas a 1% e 99%
    for col in ["roa", "tobin_q", "size", "leverage"]:
        df_clean[f"{col}_w"] = winsorize_series(df_clean[col], 0.01, 0.99)

    df_clean["did"] = df_clean["treated"] * df_clean["post"]

    # Ordenar por entidade e tempo e validar unicidade da chave do painel
    df_clean = df_clean.sort_values(["firm_id", "year"]).reset_index(drop=True)
    assert_panel_structure(df_clean, "firm_id", "year")

    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    df_clean.to_csv(PROCESSED_DATA_PATH, index=False)

    attrition_steps = [
        {"Etapa": "1. Base Bruta", "N_obs": n_raw, "Removidas": 0},
        {"Etapa": "2. Remocao de Nulos", "N_obs": n_dropna, "Removidas": n_raw - n_dropna},
        {"Etapa": "3. Painel Final", "N_obs": len(df_clean), "Removidas": 0},
    ]
    write_lineage_and_attrition(
        raw_path=RAW_DATA_PATH,
        raw_hash=raw_hash,
        attrition_steps=attrition_steps,
        panel_shape=df_clean.shape,
        n_entities=df_clean["firm_id"].nunique(),
    )
    print(f"Painel final salvo em {PROCESSED_DATA_PATH} ({len(df_clean)} obs). Lineage: PASS.")


if __name__ == "__main__":
    main()
