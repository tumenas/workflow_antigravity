---
trigger: always_on
description: Princípios invioláveis, hierarquia de decisão e limites de escopo do projeto
---
# Meta-Governance — Regras Gerais de Integridade do Projeto

## Princípios Invioláveis

1. **Nunca modificar dados brutos.** `data/raw/` é read-only. Qualquer transformação deve produzir saída em `data/processed/`.
2. **Verificar antes de concluir.** Toda tarefa termina com uma confirmação de que o output esperado foi gerado e está correto.
3. **Uma fonte de verdade.** `manuscript/manuscript.qmd` é o documento autoritativo. PDFs e HTMLs são derivados; nunca editar os derivados diretamente.
4. **Planejar antes de executar.** Para qualquer tarefa não-trivial (>1h ou >3 arquivos), criar um plano em `quality_reports/plans/YYYY-MM-DD_descricao.md` antes de iniciar.
5. **Registrar aprendizados.** Quando uma correção for feita, adicionar `[LEARN:categoria] errado → correto` em `.agents/MEMORY.md`.

## Hierarquia de Decisão

Quando houver conflito entre instruções:

1. Instruções explícitas do usuário na sessão atual — máxima prioridade
2. Regras neste diretório (`.agents/rules/`)
3. Conteúdo de `.agents/MEMORY.md`
4. Comportamento padrão do assistente

## Limites de Escopo

- Scripts de análise devem ser colocados exclusivamente em `analysis/`.
- Figuras geradas por código sempre vão para `results/figures/`.
- Tabelas geradas por código sempre vão para `results/tables/`.
- Explorations e rascunhos não revisados vão para `explorations/`.

## Comunicação

- Usar português (pt-BR) na comunicação com o usuário.
- Usar inglês nos nomes de variáveis, funções e comentários de código.
- Usar inglês nos cabeçalhos do manuscrito Quarto (YAML frontmatter).
