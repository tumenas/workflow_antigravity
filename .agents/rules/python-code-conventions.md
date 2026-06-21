# Python Code Conventions — Boas Práticas de Código Python

## Quando Usar Python neste Projeto

Python é a linguagem primária deste projeto, utilizada para:
- Processamento e limpeza de dados (`pandas`, `numpy`)
- Análises estatísticas gerais e modelagem (`scipy`, `statsmodels`, `scikit-learn`)
- Visualização de dados (`matplotlib`, `seaborn`, `plotly`)
- Automação de workflow e scripts de utilidade

Scripts Python devem seguir o padrão de numeração sequencial:
- `analysis/01_clean_data.py`, `analysis/02_analysis.py`, etc.

## Convenções de Código

### Estrutura de Script
```python
"""
Script 01: [Descrição da funcionalidade]
Lê de: data/raw/dados.csv
Escreve em: data/processed/dados_limpos.csv
"""

import os
import pandas as pd
import numpy as np

# Configurar caminhos relativos ao diretório raiz do projeto
# Sempre usar caminhos relativos para garantir portabilidade
INPUT_PATH = os.path.join("data", "raw", "dados.csv")
OUTPUT_PATH = os.path.join("data", "processed", "dados_limpos.csv")

def main():
    # Lógica principal aqui
    pass

if __name__ == "__main__":
    main()
```

### Reprodutibilidade
- Sempre fixar semente: `np.random.seed(42)` ou `random.seed(42)` no início de scripts estocásticos.
- Nunca usar caminhos absolutos ou `os.chdir()`. Usar `os.path.join` ou `pathlib.Path`.
- Requisitos: manter `requirements.txt` atualizado com as dependências do projeto.

### Estilo
- Seguir o **PEP 8**.
- Nomear variáveis, funções e arquivos em `snake_case`.
- Constantes globais (como caminhos) em `UPPER_CASE`.
- Usar docstrings para documentar o propósito de scripts e funções.
- Preferir operações vetorizadas do pandas/numpy em vez de loops `for` em DataFrames.

### Saídas
- Gráficos: salvar em `results/figures/` com alta resolução (ex: `plt.savefig(path, dpi=300, bbox_inches='tight')`).
- Tabelas: salvar em `results/tables/` usando `df.to_csv(index=False)` ou `df.to_excel()`.
- Modelos: salvar objetos serializados em `results/` usando `joblib` ou `pickle` (com cautela).

## Integração com o Workflow

Scripts Python são chamados via `Makefile` ou `run.ps1` usando:
```powershell
python analysis/01_clean_data.py
```
