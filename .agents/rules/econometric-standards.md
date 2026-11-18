---
trigger: model_decision
description: Padrões econométricos obrigatórios para scripts em src/4_econometric_analysis/ e src/5_robustness_checks/
---
# Econometric Standards

- Sempre declarar explicitamente o nível de clusterização dos erros-padrão (ex.: firma, município, ou two-way).
- Sempre listar os efeitos fixos absorvidos (Firma FE, Ano FE, Setor-Ano FE).
- Reportar número de observações ($N$), número de clusters e $R^2$ ajustado (ou within-$R^2$) em todas as tabelas.
- Documentar qualquer winsorização (ex.: 1%/99%) no `data/codebook.md` e nas notas das tabelas.
