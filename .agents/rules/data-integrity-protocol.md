---
trigger: always_on
description: Protocolo inviolável de integridade de dados — proíbe fallbacks silenciosos, exige validação de deflacionamento, merges e estrutura de painel.
---
# Data Integrity Protocol — Integridade de Dados

## Princípios Invioláveis

1. **Proibição Absoluta de Fallbacks Silenciosos:**
   - É estritamente proibido capturar erros de leitura de arquivos ou APIs (`try/except`) para gerar dados sintéticos (`np.random`), mocks ou valores padrão. Se o dado bruto falhar, o script deve interromper imediatamente com erro explícito.
   - Nunca usar `fillna(0)` ou `fillna(mean)` de forma silenciosa em variáveis econômicas/financeiras. Qualquer imputação deve ser explicitamente justificada no `data/codebook.md` e no manuscrito.
2. **Validação Sequencial Obrigatória:**
   - Todo script em `src/2_data_treatment/` deve importar `src/utils/data_assertions.py` e validar:
     - Existência e hash dos arquivos em `data/raw/`.
     - Deflacionamento de séries monetárias (quando aplicável).
     - Integridade de merges (zero explosão many-to-many acidental; registro de atrito em `results/tables/sample_attrition.csv`).
     - Unicidade da chave `(entidade, tempo)` no painel final em `data/processed/`.
3. **Bloqueio de Estimação:**
   - Nenhuma regressão em `src/4_econometric_analysis/` deve ser considerada válida se `results/logs/data_lineage_report.md` não registrar `STATUS: PASS`.
