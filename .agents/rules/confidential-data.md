---
trigger: model_decision
description: Regras de proteção para dados restritos, proprietários ou com PII (Economatica, Bloomberg, RAIS, etc.)
---
# Confidential Data Rules

- Nunca commitar microdados proprietários ou restritos no Git nem copiá-los para `replication_package/`.
- Quando houver dados restritos, documentar o processo de acesso institucional/DUA em `replication_package/access_restricted_data.md`.
- Garantir supressão/arredondamento de células pequenas antes de exportar qualquer tabela derivada de dados confidenciais.
