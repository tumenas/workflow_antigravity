# Skill: humanize

**Descrição:** Auditoria read-only da prosa acadêmica para detectar padrões típicos de linguagem gerada por IA. Não reescreve — apenas identifica e sinaliza para o autor revisar manualmente.

**Como invocar:** `humanize manuscript/manuscript.qmd`

---

## Padrões de Linguagem de IA a Detectar

### Vocabulário Marcador
Sinalizar ocorrências de palavras e expressões associadas a texto gerado por IA:
- "É importante notar que", "Vale ressaltar que", "É fundamental destacar"
- "Ademais", "Outrossim", "Destarte", "Nesse sentido"
- "Em suma", "Em conclusão" no meio de seções (não apenas no final)
- "Abrangente", "robusto", "inovador", "paradigmático" usados genericamente
- "No âmbito de", "no contexto de" repetidamente
- "Podemos observar que", "É possível perceber que"

### Padrões Estruturais
- Parágrafos que começam com "Primeiramente... Em segundo lugar... Por fim..."
- Listas de três itens onde o terceiro é redundante com os dois primeiros
- Frases que terminam com "...demonstrando assim a importância de X"
- Repetição de palavras-chave do parágrafo anterior no início do próximo

### Tom e Registro
- Assertividade excessiva sem citação (ex: "É amplamente reconhecido que...")
- Hedging excessivo (ex: "pode potencialmente talvez sugerir")
- Linguagem evasiva onde o texto deveria ser direto sobre um resultado

---

## Formato de Reporte

```
[PADRÃO AI] §Introdução, parágrafo 2:
  Trecho: "É importante notar que os resultados demonstram..."
  Padrão: frase de enchimento sem conteúdo novo
  Sugestão do autor: Reformular com o resultado em si como sujeito.

[PADRÃO AI] §Discussão, parágrafo 4:
  Trecho: "Ademais, cabe destacar que..."
  Padrão: marcador de transição característico de IA
  Sugestão do autor: Substituir por transição baseada no conteúdo lógico da frase.
```

**Ao final:** contagem de ocorrências por tipo. Não editar o arquivo — apenas reportar.
