# Compêndio de Pesquisa (Research Compendium)

Este repositório contém o código, os dados e o manuscrito para o projeto: **[Inserir Título do Artigo Aqui]**.

A organização segue o padrão **[Research Compendium](https://research-compendium.science/)**, complementado com ferramentas acadêmicas de controle de qualidade inspiradas no **[claude-code-my-workflow](https://research-compendium.science/)**, garantindo reprodutibilidade, transparência e revisão científica rigorosa.

---

## 📁 Estrutura do Repositório

```text
workflow/
├── .agents/                     # Configuração do assistente de IA
│   ├── ANTIGRAVITY.md           # Manual do assistente para este projeto
│   ├── MEMORY.md                # Memória persistente entre sessões
│   ├── settings.json            # Configurações e caminhos do projeto
│   ├── rules/                   # Regras sempre ativas de comportamento
│   │   ├── meta-governance.md   # Princípios invioláveis
│   │   ├── quality-gates.md     # Critérios de qualidade (80/90/95)
│   │   ├── cross-artifact-review.md  # Consistência código ↔ manuscrito
│   │   ├── post-flight-verification.md  # Checklist pós-execução
│   │   ├── proofreading-protocol.md  # Protocolo de revisão de escrita
│   │   ├── python-code-conventions.md # Boas práticas de código Python
│   │   ├── r-code-conventions.md     # Boas práticas de código R
│   │   └── verification-protocol.md  # Verificação final de sanidade
│   └── skills/                  # Habilidades acadêmicas sob demanda
│       ├── review-paper.md      # Revisão científica completa (3 modos)
│       ├── seven-pass-review.md # Revisão em 7 lentes paralelas
│       ├── verify-claims.md     # Verificação cruzada de dados e texto
│       ├── proofread.md         # Revisão gramatical e de estilo
│       ├── humanize.md          # Detecção de linguagem de IA
│       ├── lit-review.md        # Estruturação de revisão de literatura
│       ├── research-ideation.md # Ideação e especificação de modelos
│       ├── interview-me.md      # Entrevista socrática de metodologia
│       ├── qa-quarto.md         # QA do documento Quarto compilado
│       └── tufte-viz.md         # Ideação e crítica de gráficos (Tufte)
│
├── data/                        # Dados do projeto
│   ├── raw/                     # DADOS BRUTOS (originais, SOMENTE LEITURA)
│   └── processed/               # Dados processados (gerados por código)
│
├── analysis/                    # Scripts de análise (Python + R opcional)
│   ├── 01_clean_data.py         # Limpeza e preparação dos dados
│   ├── 02_analysis.py           # Modelagem estatística e resultados
│   └── 03_plots.py              # Geração de gráficos (300 DPI)
│
├── manuscript/                  # Artigo científico
│   ├── manuscript.qmd           # Manuscrito dinâmico em Quarto
│   ├── references.bib           # Referências em BibTeX
│   └── _quarto.yml              # Configuração de exportação (→ docs/)
│
├── results/                     # Resultados gerados pelos scripts
│   ├── figures/                 # Gráficos para o manuscrito
│   └── tables/                  # Tabelas descritivas e de modelo
│
├── quality_reports/             # Planos, logs e relatórios de qualidade
│   ├── plans/                   # Planos de tarefas
│   ├── specs/                   # Especificações de requisitos
│   ├── session_logs/            # Logs de sessões de trabalho
│   └── peer_reviews/            # Relatórios de revisão por pares
│
├── explorations/                # Sandbox de rascunhos e experimentos
├── scripts/                     # Scripts utilitários
│   └── validate-setup.ps1       # Validação do ambiente (PowerShell)
│
├── docs/                        # Manuscrito compilado (gerado pelo Quarto)
├── .gitignore                   # Arquivos excluídos do Git
├── LICENSE                      # Licenças (MIT / CC0 / CC-BY-4.0)
├── Makefile                     # Orquestrador multiplataforma (GNU Make)
├── README.md                    # Este arquivo
└── requirements.txt             # Dependências Python
```

---

## 🚀 Como Usar Este Compêndio

### Pré-requisitos

| Ferramenta | Instalação | Necessidade |
|------------|-----------|-------------|
| **Python 3.8+** | [python.org](https://python.org) | Obrigatório |
| **Quarto CLI** | [quarto.org](https://quarto.org/docs/get-started/) | Obrigatório |
| **Git** | [git-scm.com](https://git-scm.com) | Obrigatório |
| **R** | [r-project.org](https://www.r-project.org) | Opcional |

Validar o ambiente com:
```powershell
.\scripts\validate-setup.ps1
```

---

### Executando no Windows (PowerShell)

```powershell
# 1. Configurar ambiente virtual Python e instalar dependências
.\run.ps1 env

# 2. Executar toda a pipeline de análise de dados
.\run.ps1 analysis

# 3. Compilar o manuscrito (gera HTML e PDF em docs/)
.\run.ps1 paper

# 4. Pipeline completa (env + analysis + paper)
.\run.ps1 all

# 5. Limpar arquivos temporários e compilados
.\run.ps1 clean
```

### Executando via Makefile (Linux/macOS/Git Bash)

```bash
make env        # Ambiente virtual + dependências
make analysis   # Pipeline de análise
make paper      # Compilar manuscrito
make all        # Pipeline completa
make clean      # Limpar temporários
```

---

## 🧠 Habilidades Acadêmicas do Assistente

Este compêndio inclui instruções para o assistente de IA em `.agents/skills/`. Para usar qualquer habilidade, abra uma conversa com o assistente e informe o nome da habilidade e o arquivo-alvo:

| Habilidade | O que faz |
|------------|-----------|
| `review-paper` | Revisão científica completa: single-pass, adversarial ou peer review simulado |
| `seven-pass-review` | Revisão em 7 lentes paralelas (abstract, intro, métodos, resultados, robustez, prosa, referências) |
| `verify-claims` | Rastreia cada número do manuscrito até sua fonte nos dados processados |
| `proofread` | Revisão gramatical, ortográfica e de estilo acadêmico |
| `humanize` | Detecta padrões de linguagem de IA na prosa científica |
| `lit-review` | Estrutura busca e síntese de literatura |
| `research-ideation` | Brainstorming de questões, modelos e robustez |
| `interview-me` | Entrevista socrática para clarificar metodologia |
| `qa-quarto` | Revisão adversarial do documento Quarto compilado |
| `tufte-viz` | Ideação e crítica de gráficos com base nos princípios de Edward Tufte |

---

## 📜 Licenciamento

| Componente | Licença |
|------------|---------|
| Código e scripts (`analysis/`) | [MIT](LICENSE) |
| Dados (`data/`) | [CC0 1.0](LICENSE) (Domínio Público) |
| Manuscrito e figuras (`manuscript/`, `results/`) | [CC-BY 4.0](LICENSE) |
