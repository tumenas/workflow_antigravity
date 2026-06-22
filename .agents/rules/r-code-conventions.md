---
trigger:
  files:
    - "**/*.R"
    - "**/*.r"
description: Diretrizes de estilo e qualidade para escrita de código R
---
# R Code Conventions — Boas Práticas de Código R

## Quando Usar R neste Projeto

R é utilizado como linguagem secundária, principalmente para:
- Análises estatísticas específicas do ecossistema R (ex: `lme4`, `lavaan`, `fixest`)
- Visualizações avançadas com `ggplot2`
- Scripts de replicação de metodologias publicadas originalmente em R

Scripts R devem seguir o mesmo padrão de numeração sequencial dos scripts Python:
- `analysis/04_r_analysis.R`, `analysis/05_r_plots.R`, etc.

## Convenções de Código

### Estrutura de Script
```r
# =============================================================================
# Script 04: [Descrição da análise]
# Lê de: data/processed/dados_processados.csv
# Escreve em: results/tables/ e results/figures/
# =============================================================================

library(tidyverse)
library(here)   # sempre usar here::here() para caminhos

# Caminhos
processed_path <- here("data", "processed", "dados_processados.csv")
tables_dir     <- here("results", "tables")
figures_dir    <- here("results", "figures")
```

### Reprodutibilidade
- Sempre fixar semente: `set.seed(42)` no início de cada script que usa aleatoriedade.
- Usar `here::here()` para todos os caminhos de arquivo — nunca caminhos absolutos ou `setwd()`.
- Registrar pacotes utilizados com `sessionInfo()` ao final do script (salvar em `results/tables/session_info.txt`).

### Estilo
- Usar tidyverse e pipe `|>` (nativo R 4.1+) em vez de `%>%` quando possível.
- Nomear objetos em `snake_case`.
- Funções customizadas devem ter documentação roxygen mínima.
- Evitar loops `for` onde `purrr::map()` for mais claro.

### Saídas
- Gráficos: salvar com `ggsave()` em `results/figures/` com `dpi = 300`, `width` e `height` explícitos.
- Tabelas: salvar com `write_csv()` em `results/tables/` — nunca apenas imprimir no console.
- Modelos: se o objeto de modelo for reutilizado, salvar com `saveRDS()` em `results/`.

## Integração com o Makefile

Adicionar chamadas a scripts R no `Makefile` e `run.ps1` usando:
```powershell
Rscript analysis/04_r_analysis.R
```
