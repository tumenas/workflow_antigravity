# Project Memory

Correções e fatos aprendidos que persistem entre sessões.
Quando um erro for corrigido ou convenção estabelecida, adicione um registro `[LEARN:categoria]` abaixo.
Entradas mais recentes no final do arquivo.

---

## Padrões de Workflow

[LEARN:workflow] Fase de especificação captura ambiguidade antes do planejamento → reduz retrabalho em 30-50%. Use spec-depois-plan para tarefas complexas (>1h ou >3 arquivos).

[LEARN:workflow] Protocolo spec-depois-plan: 3-5 perguntas → cria `quality_reports/specs/YYYY-MM-DD_descricao.md` com requisitos MUST/SHOULD/MAY → declara CLEAR/ASSUMED/BLOCKED → aprovação → rascunha plano.

[LEARN:workflow] Planos, specs e logs de sessão devem estar em disco (não apenas na conversa) para sobreviver a compressão de contexto e limites de sessão.

[LEARN:data] NUNCA modificar arquivos em `data/raw/`. Todo pré-processamento gera saída em `data/processed/`.

## Padrões de Documentação

[LEARN:documentation] Ao adicionar novos recursos, atualizar README imediatamente para evitar documentação desatualizada.

[LEARN:documentation] Campos de data no frontmatter do `manuscript.qmd` devem usar `last-modified` do Quarto para atualização automática.

## Convenções de Código Python

[LEARN:python] Scripts de análise devem ser numerados sequencialmente (01_, 02_, 03_) e cada um salvar sua saída antes de encerrar — nunca deixar resultados apenas em memória.

[LEARN:python] Gráficos gerados por `03_plots.py` devem ser salvos com `dpi=300` e `bbox_inches="tight"` para qualidade de impressão científica.

[LEARN:python] Estatísticas descritivas e coeficientes de regressão devem ser salvos em `results/tables/` como CSV para importação dinâmica no manuscrito Quarto.

## Convenções do Manuscrito Quarto

[LEARN:quarto] O arquivo `manuscript/_quarto.yml` define `output-dir: ../docs` — nunca alterar este caminho sem atualizar o Makefile e run.ps1.

[LEARN:quarto] Figuras referenciadas no manuscrito devem usar caminhos relativos a partir da pasta `manuscript/` (ex: `../results/figures/nome.png`).

[LEARN:quarto] Rótulos de figuras (`#fig-`) e tabelas (`#tbl-`) no Quarto devem ser únicos em todo o documento.

[LEARN:workflow] Arquivos de skills em `.agents/skills/` devem sempre referenciar caminhos sob `.agents/rules/` e nunca sob a pasta antiga `.antigravitycli/rules/`.

[LEARN:antigravity] Regras individuais em `.agents/rules/` exigem cabeçalho YAML frontmatter com `trigger` definido (ex: `always_on` ou padrão de `files`) para serem descobertas e carregadas automaticamente pelo Antigravity.

[LEARN:antigravity] O arquivo `.agents/hooks.json` deve conter os eventos de hooks (`PreToolUse`, `PostToolUse`, etc.) mapeados diretamente no nível raiz do objeto JSON, e não envelopados sob a chave `"workspace-hooks"`.

[LEARN:python] Scripts executados no terminal Windows (CMD/PowerShell) devem evitar caracteres unicode não-ASCII (como '↳') em saídas impressas de texto, pois geram exceções UnicodeEncodeError sob codificação CP1252. Use alternativas ASCII (como '->').

