---
trigger: model_decision
description: Protocolo de replicação AEA/DCAS — tolerância zero para divergência entre código, tabelas e manuscrito.
---
# Replication Protocol

- **Consistência Numérica:** Todo número citado no texto de `manuscript/manuscript.qmd` deve corresponder exatamente aos arquivos em `results/tables/` gerados por `python src/00_master.py`.
- **Portabilidade:** Nunca usar caminhos absolutos (`C:\Users\...` ou `/home/...`) nem `os.chdir()` / `setwd()`.
- **Rastreabilidade:** Manter atualizado o mapeamento Tabela/Figura -> Script em `replication_package/README_replication.md`.
