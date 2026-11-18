# Compêndio de Pesquisa (Research Compendium) — Economia, Finanças e Administração

Este repositório é um **modelo estruturado** para artigos empíricos na área de **Economia, Finanças e Administração**, seguindo o padrão **[Research Compendium](https://research-compendium.science/)** e as diretrizes de reprodutibilidade da **AEA Data and Code Availability Standard (DCAS)**.

---

## 📁 Estrutura do Repositório

```text
workflow/
├── .agents/                          # Configuração do assistente de IA (AGENTS.md, MEMORY.md, rules/, skills/)
├── data/
│   ├── raw/                          # Dados brutos originais (READ-ONLY)
│   ├── external/                     # Tabelas auxiliares (deflatores IPCA, CNAE/GICS, códigos IBGE)
│   ├── intermediate/                 # Bases limpas individualmente antes do merge
│   ├── processed/                    # Painel/dataset final pronto para econometria
│   └── codebook.md                   # Dicionário de variáveis (fórmula, fonte, unidade)
├── src/                              # Pipeline de código modularizada
│   ├── 00_master.py                  # Script mestre que executa toda a pipeline em sequência
│   ├── utils/                        # Funções compartilhadas (winsorize, estilo de gráficos)
│   ├── 1_data_collection/            # Coleta de dados / APIs / queries
│   ├── 2_data_treatment/             # Limpeza, deflação, winsorização e merge do painel
│   ├── 3_exploratory_analysis/       # Tabela 1 (descritivas), correlações e gráficos EDA
│   ├── 4_econometric_analysis/       # Modelos baseline e identificação (DiD, FE, IV, RDD, GMM)
│   ├── 5_robustness_checks/          # Testes de robustez, placebo e especificações alternativas
│   └── 6_tables_and_figures/         # Geração final de figuras (300 DPI) e tabelas de publicação
├── results/
│   ├── figures/                      # Figuras finais para o manuscrito e slides
│   ├── tables/                       # Tabelas (.csv, .tex, .md)
│   ├── models/                       # Estimativas salvas de modelos pesados
│   └── logs/                         # Logs de execução
├── manuscript/
│   ├── manuscript.qmd                # Artigo principal (Quarto)
│   ├── online_appendix.qmd           # Apêndice Online
│   ├── title_page.qmd                # Folha de rosto separada (double-blind review)
│   ├── cover_letter.md               # Carta de submissão ao editor
│   ├── referee_response.qmd          # Template de resposta aos pareceristas (R&R)
│   ├── references.bib                # Bibliografia BibTeX
│   └── _quarto.yml                   # Configuração de exportação (→ docs/)
├── presentations/
│   └── slides.qmd                    # Template de apresentação (Reveal.js)
├── literature/
│   ├── literature_matrix.md          # Matriz de síntese da literatura
│   └── pdfs/                         # PDFs de referência (ignorado no Git)
├── replication_package/
│   ├── README_replication.md         # README padrão AEA/DCAS
│   ├── DCAS_checklist.md             # Checklist de conformidade
│   └── access_restricted_data.md     # Nota de acesso para dados proprietários
├── quality_reports/                  # Planos, specs, logs de sessão e peer reviews
├── explorations/                     # Sandbox para testes rápidos
├── scripts/                          # Scripts utilitários (validate-setup.ps1)
├── Makefile                          # Orquestrador Make
├── run.ps1                           # Orquestrador Windows PowerShell
└── requirements.txt                  # Dependências Python
```

---

## 🚀 Como Usar Este Compêndio

### 1. Executar a pipeline empírica completa
```powershell
python src/00_master.py
```
Ou usando o orquestrador PowerShell:
```powershell
.\run.ps1 analysis
```

### 2. Compilar o manuscrito ou apresentação (Quarto)
```powershell
.\run.ps1 paper
.\run.ps1 slides
```
