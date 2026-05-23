# Skill: proofread

**Descrição:** Revisão detalhada de gramática, ortografia, estilo acadêmico e fluidez do manuscrito. Não altera conteúdo científico, apenas a forma da escrita.

**Como invocar:** `proofread manuscript/manuscript.qmd` ou `proofread [seção específica]`

---

## Protocolo

Aplicar `.antigravitycli/rules/proofreading-protocol.md` integralmente no arquivo informado.

### Processo

1. **Leitura completa** — ler o texto sem marcar, para captar o fluxo geral.
2. **Revisão de sentença** — verificar gramática, ortografia e pontuação.
3. **Revisão de parágrafo** — verificar coesão e transições.
4. **Revisão de seção** — verificar progressão lógica e consistência terminológica.
5. **Relatório** — listar todos os problemas encontrados no formato definido.

### Prioridades de Correção

🔴 **Alta**: erros gramaticais que comprometem a compreensão; inconsistências terminológicas graves.
🟡 **Média**: frases excessivamente longas; uso inadequado de voz passiva; redundâncias.
🟢 **Baixa**: preferências estilísticas; sugestões de variação lexical.

### Limitações

- NÃO alterar valores numéricos — ver `verify-claims` para isso.
- NÃO reorganizar seções — isso requer aprovação explícita do usuário.
- NÃO reescrever parágrafos inteiros sem solicitação — apenas sinalizar e sugerir.

### Formato de Saída

```
[ALTA] §Introdução, §2, linha ~3
  Original:  "Os dados foram coletados sendo que as amostras foram analisadas..."
  Sugestão:  "Os dados foram coletados e as amostras foram analisadas..."
  Motivo:    Construção redundante com gerúndio desnecessário.

[MÉDIA] §Metodologia, §1
  Original:  "Foi realizada uma análise..."
  Sugestão:  "Realizamos uma análise..." ou "A análise foi realizada..."
  Motivo:    Voz passiva despersonalizada; verificar estilo do periódico-alvo.
```

Ao final: **contagem total** de problemas por prioridade.
