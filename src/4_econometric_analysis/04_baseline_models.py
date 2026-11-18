"""
Etapa 4: Análise Econométrica Principal (Econometric Analysis).
Estima modelo Diff-in-Diff com efeitos fixos de firma e ano.
Salva coeficientes em results/tables/coeficientes_baseline.csv.
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

    # Modelo Diff-in-Diff com Efeitos Fixos de Firma e Ano e erros-padrão clusterizados por firma
    formula = "roa_w ~ did + size_w + leverage_w + C(firm_id) + C(year)"
    model = smf.ols(formula, data=df).fit(
        cov_type="cluster",
        cov_kwds={"groups": df["firm_id"]}
    )

    # Extrair apenas as variáveis explicativas principais (omitindo dummies de FE na tabela)
    main_vars = ["did", "size_w", "leverage_w"]
    summary_df = pd.DataFrame({
        "Variavel": main_vars,
        "Coeficiente": [round(model.params[v], 4) for v in main_vars],
        "Erro_Padrao": [round(model.bse[v], 4) for v in main_vars],
        "t_stat": [round(model.tvalues[v], 3) for v in main_vars],
        "p_valor": [round(model.pvalues[v], 4) for v in main_vars],
        "N_obs": int(model.nobs),
        "R2_ajustado": round(model.rsquared_adj, 4),
    })

    coef_path = os.path.join(TABLES_DIR, "coeficientes_baseline.csv")
    summary_df.to_csv(coef_path, index=False)
    print(f"Resultados baseline salvos em: {coef_path}")
    print(summary_df.to_string(index=False))


if __name__ == "__main__":
    main()
