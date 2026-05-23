"""
Script 02: Modelagem e Análise Estatística.
Lê os dados limpos de `data/processed/` e executa análises estatísticas e regressões.
Salva tabelas de resultados em `results/tables/`.
"""

import os
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Caminhos dos arquivos
PROCESSED_DATA_PATH = os.path.join("data", "processed", "dados_processados.csv")
TABLES_DIR = os.path.join("results", "tables")

def main():
    # 1. Carregar dados limpos
    if not os.path.exists(PROCESSED_DATA_PATH):
        raise FileNotFoundError(f"Dados limpos não encontrados em {PROCESSED_DATA_PATH}. Rode o script 01_clean_data.py primeiro.")
        
    df = pd.read_csv(PROCESSED_DATA_PATH)
    print("Dados carregados com sucesso para modelagem.")
    
    # Garantir que a pasta de resultados existe
    os.makedirs(TABLES_DIR, exist_ok=True)
    
    # 2. Estatísticas Descritivas por Grupo
    print("Gerando estatísticas descritivas...")
    tabela_descritiva = df.groupby("grupo")[["idade", "pressao_arterial", "marcador_biologico"]].mean().round(2)
    
    # Salvar tabela descritiva em formato CSV
    descritiva_path = os.path.join(TABLES_DIR, "tabela_descritiva.csv")
    tabela_descritiva.to_csv(descritiva_path)
    print(f"Tabela descritiva salva em: {descritiva_path}")
    
    # 3. Modelagem Estatística (Regressão Linear)
    print("Ajustando modelo de Regressão Linear Múltipla...")
    # Modelo: pressao_arterial explicada por idade, marcador_biologico e grupo
    model = smf.ols("pressao_arterial ~ idade + marcador_biologico + C(grupo)", data=df)
    results = model.fit()
    
    # Imprimir resumo do modelo no console
    print(results.summary())
    
    # Salvar o resumo em arquivo TXT
    results_txt_path = os.path.join(TABLES_DIR, "resultado_regressao.txt")
    with open(results_txt_path, "w", encoding="utf-8") as f:
        f.write(results.summary().as_text())
        
    # Salvar coeficientes em tabela CSV para importação direta
    coef_df = results.summary2().tables[1].round(4)
    coef_path = os.path.join(TABLES_DIR, "coeficientes_regressao.csv")
    coef_df.to_csv(coef_path)
    
    print(f"Resultados da regressão salvos em: {results_txt_path} e {coef_path}")

if __name__ == "__main__":
    main()
