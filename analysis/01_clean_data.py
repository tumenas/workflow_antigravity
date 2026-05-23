"""
Script 01: Limpeza e Preparação de Dados.
Lê os dados brutos de `data/raw/` e gera dados limpos em `data/processed/`.
Caso os dados brutos não existam, gera um dataset sintético para demonstração.
"""

import os
import pandas as pd
import numpy as np

# Configurar caminhos relativos ao diretório raiz do projeto
RAW_DATA_PATH = os.path.join("data", "raw", "dados_brutos.csv")
PROCESSED_DATA_PATH = os.path.join("data", "processed", "dados_processados.csv")

def gerar_dados_sinteticos():
    """Gera dados de exemplo para permitir teste imediato da estrutura."""
    print("==> Criando dataset sintético de exemplo em data/raw/dados_brutos.csv...")
    np.random.seed(42)
    n_samples = 100
    
    dados = {
        "id_paciente": range(1, n_samples + 1),
        "grupo": np.random.choice(["Controle", "Tratamento A", "Tratamento B"], n_samples),
        "idade": np.random.randint(18, 80, n_samples),
        "pressao_arterial": np.random.normal(120, 15, n_samples).round(1),
        "marcador_biologico": np.random.normal(5.0, 1.5, n_samples).round(2),
        "resposta_tratamento": np.random.choice([0, 1], n_samples, p=[0.3, 0.7])
    }
    
    # Criar DataFrame e salvar na pasta raw
    df = pd.DataFrame(dados)
    
    # Garantir que a pasta data/raw existe
    os.makedirs(os.path.dirname(RAW_DATA_PATH), exist_ok=True)
    df.to_csv(RAW_DATA_PATH, index=False)
    print("Dataset sintético gerado com sucesso.")

def main():
    # 1. Verificar se o dado bruto existe, caso contrário, gerar dados sintéticos
    if not os.path.exists(RAW_DATA_PATH):
        gerar_dados_sinteticos()
    
    # 2. Carregar dados brutos
    print(f"Carregando dados de {RAW_DATA_PATH}...")
    df = pd.read_csv(RAW_DATA_PATH)
    
    # 3. Limpeza de dados (Exemplo)
    print("Executando passos de limpeza...")
    # Exemplo: remover registros com idades absurdas ou valores nulos
    df_clean = df.dropna()
    df_clean = df_clean[df_clean["idade"].between(18, 90)]
    
    # Exemplo: Criar uma nova variável (ex: indicador de hipertensão)
    df_clean["hipertenso"] = (df_clean["pressao_arterial"] >= 130).astype(int)
    
    # 4. Salvar dados processados
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    df_clean.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"Dados limpos salvos com sucesso em: {PROCESSED_DATA_PATH}")
    print(f"Total de registros originais: {len(df)} | Registros limpos: {len(df_clean)}")

if __name__ == "__main__":
    main()
