"""
Etapa 1: Coleta de Dados (Data Collection).
Simula a coleta de dados brutos de painel de firmas (Economia/Finanças)
e salva em data/raw/firmas_brutas.csv.
"""

import os
import numpy as np
import pandas as pd

RAW_DATA_PATH = os.path.join("data", "raw", "firmas_brutas.csv")


def generate_synthetic_firm_panel(n_firms: int = 80, start_year: int = 2016, end_year: int = 2023) -> pd.DataFrame:
    """Gera um painel sintético de firmas-ano com choque regulatório em 2020."""
    np.random.seed(42)
    years = list(range(start_year, end_year + 1))
    rows = []

    for firm_id in range(1, n_firms + 1):
        treated = 1 if firm_id <= n_firms // 2 else 0
        firm_fe = np.random.normal(0.0, 0.02)
        base_size = np.random.normal(14.0, 1.5)
        sector = np.random.choice(["Industria", "Servicos", "Varejo", "Energia"])

        for year in years:
            post = 1 if year >= 2020 else 0
            size = base_size + 0.03 * (year - start_year) + np.random.normal(0, 0.1)
            leverage = np.clip(np.random.normal(0.45, 0.15), 0.05, 0.95)
            # Efeito causal simulado do choque (treated * post = +0.025 no ROA)
            roa = (
                0.06
                + firm_fe
                + 0.005 * (size - 14.0)
                - 0.04 * leverage
                + 0.025 * (treated * post)
                + np.random.normal(0, 0.02)
            )
            tobin_q = 1.2 + 2.5 * roa - 0.3 * leverage + np.random.normal(0, 0.15)

            rows.append({
                "firm_id": firm_id,
                "year": year,
                "sector": sector,
                "treated": treated,
                "post": post,
                "roa": round(roa, 4),
                "tobin_q": round(tobin_q, 4),
                "size": round(size, 4),
                "leverage": round(leverage, 4),
            })

    return pd.DataFrame(rows)


def main() -> None:
    if os.path.exists(RAW_DATA_PATH):
        print(f"Dados brutos ja existem em {RAW_DATA_PATH}. Mantendo arquivo original (READ-ONLY).")
        return

    print("==> Gerando painel sintetico de firmas em data/raw/firmas_brutas.csv...")
    df = generate_synthetic_firm_panel()
    os.makedirs(os.path.dirname(RAW_DATA_PATH), exist_ok=True)
    df.to_csv(RAW_DATA_PATH, index=False)
    print(f"Coleta concluida: {len(df)} observacoes firma-ano salvas.")


if __name__ == "__main__":
    main()
