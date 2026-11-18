"""
Etapa 5: Testes de Robustez (Robustness Checks).
Executa teste placebo (choque ficticio em 2018 no periodo pre-tratamento)
e especificacao alternativa com Q de Tobin como variavel dependente.
"""

import os
import pandas as pd
import statsmodels.formula.api as smf

PROCESSED_DATA_PATH = os.path.join("data", "processed", "painel_final.csv")
TABLES_DIR = os.path.join("results", "tables")


def main() -> None:
    if not os.path.exists(PROCESSED_DATA_PATH):
        raise FileNotFoundError(f"Painel final nao encontrado: {PROCESSED_DATA_PATH}")

    df = pd.read_csv(PROCESSED_DATA_PATH)
    os.makedirs(TABLES_DIR, exist_ok=True)

    # 1. Teste Placebo (apenas periodo pre-2020, choque ficticio em 2018)
    df_pre = df[df["year"] < 2020].copy()
    df_pre["placebo_post"] = (df_pre["year"] >= 2018).astype(int)
    df_pre["placebo_did"] = df_pre["treated"] * df_pre["placebo_post"]

    m_placebo = smf.ols("roa_w ~ placebo_did + size_w + leverage_w + C(firm_id) + C(year)", data=df_pre).fit(
        cov_type="cluster", cov_kwds={"groups": df_pre["firm_id"]}
    )

    # 2. Variável dependente alternativa (Q de Tobin)
    m_tobin = smf.ols("tobin_q_w ~ did + size_w + leverage_w + C(firm_id) + C(year)", data=df).fit(
        cov_type="cluster", cov_kwds={"groups": df["firm_id"]}
    )

    rob_df = pd.DataFrame([
        {
            "Especificacao": "Placebo (2018, Pre-tratamento)",
            "Var_Interesse": "placebo_did",
            "Coeficiente": round(m_placebo.params["placebo_did"], 4),
            "Erro_Padrao": round(m_placebo.bse["placebo_did"], 4),
            "p_valor": round(m_placebo.pvalues["placebo_did"], 4),
            "N_obs": int(m_placebo.nobs),
        },
        {
            "Especificacao": "Var. Dependente: Q de Tobin",
            "Var_Interesse": "did",
            "Coeficiente": round(m_tobin.params["did"], 4),
            "Erro_Padrao": round(m_tobin.bse["did"], 4),
            "p_valor": round(m_tobin.pvalues["did"], 4),
            "N_obs": int(m_tobin.nobs),
        },
    ])

    rob_path = os.path.join(TABLES_DIR, "robustez.csv")
    rob_df.to_csv(rob_path, index=False)
    print(f"Testes de robustez salvos em: {rob_path}")


if __name__ == "__main__":
    main()
