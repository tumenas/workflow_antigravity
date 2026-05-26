# Cross-Artifact Review — Consistência entre Código e Manuscrito

## Objetivo

Garantir que todos os números, tabelas e figuras citados no manuscrito `manuscript/manuscript.qmd` sejam rastreáveis e reprodutíveis a partir dos scripts de análise em `analysis/`.

## Protocolo de Revisão

Ao revisar o manuscrito, verificar **cada afirmação quantitativa**:

### Passo 1 — Identificar claims no texto
Extrair todas as afirmações numéricas do manuscrito:
- Estatísticas descritivas (médias, desvios-padrão, medianas)
- Coeficientes de modelos e seus intervalos de confiança
- Valores p e estatísticas de teste
- Tamanhos de amostra e números de observações
- Porcentagens e proporções

### Passo 2 — Rastrear até a fonte
Para cada claim, identificar:
- Qual script Python/R gera este número? (ex: `02_analysis.py`)
- Qual arquivo de saída contém o resultado? (ex: `results/tables/coeficientes_regressao.csv`)
- O número no manuscrito bate exatamente com o arquivo de resultado?

### Passo 3 — Verificar propagação de figuras
Para cada figura no manuscrito:
- O arquivo referenciado existe em `results/figures/`?
- O caminho relativo no `.qmd` está correto (`../results/figures/nome.png`)?
- A figura corresponde à análise descrita no texto adjacente?

### Passo 4 — Verificar referências cruzadas internas
- Todas as figuras (`@fig-`) e tabelas (`@tbl-`) referenciadas no texto existem como blocos rotulados?
- Todas as equações (`@eq-`) são únicas e referenciadas?

## Reporte

Reportar discrepâncias encontradas como:
```
[INCONSISTÊNCIA] Manuscrito §Resultados afirma N=100, mas `01_clean_data.py` filtra para N=98.
[INCONSISTÊNCIA] Figura 2 mostra coeficiente β=0.35, mas `results/tables/coeficientes_regressao.csv` tem 0.352.
[OK] Tabela 1 estatísticas descritivas verificadas contra `results/tables/tabela_descritiva.csv`.
```
