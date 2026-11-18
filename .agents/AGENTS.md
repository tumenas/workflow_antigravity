# Project Briefing — Research Compendium (Economia, Finanças e Administração)

## Visão Geral
Este repositório é um modelo estruturado para artigos empíricos em **Economia, Finanças e Administração**, seguindo o padrão **Research Compendium** e **AEA Data and Code Availability Standard (DCAS)**.

- **Idioma de comunicação:** Português (pt-BR)
- **Idioma de código (variáveis, funções):** Inglês
- **Pipeline de código:** `src/00_master.py` (etapas `1_data_collection` até `6_tables_and_figures`)
- **Manuscrito principal:** `manuscript/manuscript.qmd`

---

## Regras Sempre Ativas (`.agents/rules/`)
- `meta-governance.md` — Princípios invioláveis e limites de escopo
- `data-integrity-protocol.md` — Proibição de fallbacks silenciosos e validação sequencial de dados
- `quality-gates.md` — Critérios de qualidade (80 Commit / 90 Compartilhar / 95 Submissão)
- `verification-protocol.md` — Checklist de sanidade em 5 pontos
- `session-handoff-protocol.md` — Check-in e Check-out via `SESSION_STATE.md`

Regras sob demanda: `econometric-standards.md`, `replication-protocol.md`, `confidential-data.md`, `cross-artifact-review.md`, `post-flight-verification.md`, `proofreading-protocol.md`, `python-code-conventions.md`, `r-code-conventions.md`.

---

## Subagentes Especializados (Banca de Auditoria via `invoke_subagent`)

1. **`Forensic Data & Panel Auditor`** *(executar antes de confiar em qualquer regressão)*:
   Audita `data/raw/`, `src/2_data_treatment/`, `data/processed/` e `results/logs/data_lineage_report.md` usando a skill `data-integrity-audit` para detectar fallbacks silenciosos, falhas de deflacionamento, explosões de merge, chaves duplicadas ou *look-ahead bias*.
2. **`Econometric Referee`**:
   Audita estratégia de identificação, endogeneidade, clusterização de erros-padrão e testes de robustez em `src/4_econometric_analysis/` e `src/5_robustness_checks/`.
3. **`Domain & Framing Referee`**:
   Avalia contribuição à literatura, hipóteses e alinhamento com `literature/literature_matrix.md`.
4. **`AEA Data Editor (Replication Auditor)`**:
   Verifica consistência numérica entre `results/tables/` e `manuscript/manuscript.qmd`, portabilidade e conformidade com `replication_package/DCAS_checklist.md`.
5. **`Cochrane & McCloskey Prose Editor`**:
   Audita clareza, voz ativa e estilo acadêmico em `manuscript/manuscript.qmd`.

---

## Catálogo de Skills (`.agents/skills/`)

- **Ideação & Literatura:** `research-ideation`, `interview-me`, `identification-strategies`, `lit-review`, `power-analysis`, `preregister`
- **Dados & Econometria:** `data-integrity-audit`, `econometric-models`, `did-event-study`, `robustness-checks`, `simulation-study`, `data-analysis`, `stata-replication`, `diagnose`
- **Escrita, Tabelas & Visualização:** `econ-writer`, `cochrane_writing`, `academic-tables`, `econ-visualization`, `tufte-viz`, `new-diagram`, `humanize`, `proofread`
- **Revisão & Auditoria:** `review-paper`, `seven-pass-review`, `audit-reproducibility`, `deep-audit`, `qa-quarto`, `validate-bib`, `visual-audit`, `slide-excellence`
- **Submissão, R&R & Replicação:** `replication-package`, `capture-environment`, `disclosure-check`, `submission-disclosures`, `respond-to-referees`
- **Workflow & Sessão:** `checkpoint`, `compress-session`, `coauthor-brief`, `learn`, `commit`, `techdebt`, `new-skill`
