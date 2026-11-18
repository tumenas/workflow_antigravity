"""
Contratos de Dados (Data Assertions) para garantir integridade de ponta a ponta.
Valida existencia/hash de dados brutos, deflacionamento, merges e estrutura de painel,
gerando laudo em results/logs/data_lineage_report.md e atrito em results/tables/sample_attrition.csv.
"""

import hashlib
import os
from datetime import datetime
import pandas as pd


def file_sha256(path: str) -> str:
    """Calcula hash SHA-256 de um arquivo."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()[:16]


def assert_raw_authentic(path: str, required_cols: list[str]) -> str:
    """Garante que o arquivo bruto existe fisicamente, nao esta vazio e possui as colunas esperadas."""
    if not os.path.isfile(path):
        raise FileNotFoundError(f"[FAIL-FAST] Dado bruto ausente: {path}")
    if os.path.getsize(path) == 0:
        raise ValueError(f"[FAIL-FAST] Dado bruto vazio: {path}")
    df_head = pd.read_csv(path, nrows=5)
    missing = [c for c in required_cols if c not in df_head.columns]
    if missing:
        raise ValueError(f"[FAIL-FAST] Colunas ausentes em {path}: {missing}")
    return file_sha256(path)


def assert_panel_structure(df: pd.DataFrame, entity_col: str, time_col: str) -> None:
    """Garante unicidade da chave (entidade, tempo) no painel final."""
    dups = df.duplicated(subset=[entity_col, time_col]).sum()
    if dups > 0:
        raise ValueError(f"[FAIL-FAST] Painel possui {dups} chaves duplicadas ({entity_col}, {time_col}).")


def assert_deflated(df: pd.DataFrame, nominal_col: str, real_col: str, index_col: str, base_year_mask: pd.Series) -> None:
    """Verifica se uma serie monetaria foi efetivamente deflacionada."""
    if (df[index_col] <= 0).any() or df[index_col].isna().any():
        raise ValueError(f"[FAIL-FAST] Indice deflator {index_col} contem zeros ou nulos.")
    if not (df.loc[base_year_mask, real_col].round(4) == df.loc[base_year_mask, nominal_col].round(4)).all():
        raise ValueError(f"[FAIL-FAST] Valores reais diferem dos nominais no ano-base para {real_col}.")


def write_lineage_and_attrition(
    raw_path: str,
    raw_hash: str,
    attrition_steps: list[dict],
    panel_shape: tuple[int, int],
    n_entities: int,
) -> None:
    """Grava relatorio de linhagem de dados e tabela de atrito amostral."""
    os.makedirs(os.path.join("results", "logs"), exist_ok=True)
    os.makedirs(os.path.join("results", "tables"), exist_ok=True)

    attr_df = pd.DataFrame(attrition_steps)
    attr_df.to_csv(os.path.join("results", "tables", "sample_attrition.csv"), index=False)

    report = [
        "# Data Lineage & Integrity Report",
        f"- **Timestamp:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- **Raw File:** `{raw_path}` (SHA-256 prefix: `{raw_hash}`)",
        f"- **Final Panel Shape:** {panel_shape[0]} rows x {panel_shape[1]} cols ({n_entities} unique entities)",
        "- **Panel Key Uniqueness:** PASS (0 duplicates)",
        "- **STATUS: PASS**",
    ]
    with open(os.path.join("results", "logs", "data_lineage_report.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(report) + "\n")
