# Post-Flight Verification — Verificação Pós-Execução

## Objetivo

Após rodar qualquer script de análise ou renderizar o manuscrito, executar este protocolo de verificação antes de declarar a tarefa concluída.

## Checklist Pós-Execução de Scripts Python

Após rodar `.\run.ps1 analysis` ou qualquer script individualmente:

- [ ] Os arquivos de saída esperados existem?
  - `data/processed/dados_processados.csv` (após `01_clean_data.py`)
  - `results/tables/tabela_descritiva.csv` (após `02_analysis.py`)
  - `results/tables/coeficientes_regressao.csv` (após `02_analysis.py`)
  - `results/figures/boxplot_marcador_grupo.png` (após `03_plots.py`)
  - `results/figures/dispersao_pressao_idade.png` (após `03_plots.py`)
- [ ] Nenhum script terminou com erro ou traceback?
- [ ] Os outputs têm tamanho razoável (arquivos não-vazios)?
- [ ] A semente aleatória está fixada onde necessário para reprodutibilidade?

## Checklist Pós-Renderização do Manuscrito

Após rodar `.\run.ps1 paper` ou `quarto render manuscript/manuscript.qmd`:

- [ ] O arquivo de saída foi gerado em `docs/`?
- [ ] Todas as figuras aparecem no documento compilado?
- [ ] Todas as tabelas estão formatadas corretamente?
- [ ] As referências bibliográficas estão formatadas (não aparecem como `[?]`)?
- [ ] As equações são renderizadas corretamente (não aparecem como texto LaTeX cru)?
- [ ] As referências cruzadas internas (`@fig-`, `@tbl-`, `@eq-`) resolvem corretamente?
- [ ] Nenhuma seção aparece vazia ou com conteúdo de placeholder?

## Em Caso de Falha

1. Identificar o erro exato (mensagem de erro, linha do script, arquivo afetado).
2. Corrigir a causa raiz — nunca contornar sem entender a origem.
3. Re-executar e repetir este checklist.
4. Registrar em `.antigravitycli/MEMORY.md` se o erro revelar um padrão recorrente.
