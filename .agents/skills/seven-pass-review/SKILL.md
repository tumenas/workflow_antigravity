# Skill: seven-pass-review

**Descrição:** Revisão de sete lentes independentes em paralelo, depois sintetizada. Mais pesada que `review-paper` (custo de contexto ~7×). Indicada para rascunhos prontos para submissão ou estágio de R&R onde máxima cobertura é necessária.

**Como invocar:** `seven-pass-review manuscript/manuscript.qmd`

---

## As Sete Lentes

Conduzir cada revisão de forma independente, sem consultar as outras:

### Lente 1 — Abstract e Primeira Impressão
- O abstract resume fielmente o artigo completo?
- A questão de pesquisa, metodologia, resultados e conclusão aparecem no abstract?
- Um leitor externo conseguiria decidir se quer ler o artigo inteiro com base apenas no abstract?

### Lente 2 — Introdução e Motivação
- O problema de pesquisa está claramente definido?
- A lacuna na literatura está identificada e justificada?
- A contribuição do artigo é explicitada antes de terminar a introdução?
- O mapa do artigo (estrutura das seções) está presente?

### Lente 3 — Metodologia
- Os dados são descritos com detalhe suficiente para reprodução?
- O design metodológico responde à questão de pesquisa proposta?
- As hipóteses ou questões de pesquisa são testáveis com os métodos escolhidos?
- As limitações metodológicas são reconhecidas?

### Lente 4 — Resultados
- Os resultados são apresentados de forma ordenada e coerente com a metodologia?
- Tabelas e figuras são auto-explicativas (legendas completas, rótulos claros)?
- Todos os resultados reportados no texto existem nas tabelas/figuras?
- Os tamanhos de efeito são reportados, não apenas valores p?

### Lente 5 — Robustez e Validade
- Análises de sensibilidade ou robustez são realizadas?
- Os resultados principais mudam substancialmente com especificações alternativas?
- Ameaças à validade interna e externa são discutidas?

### Lente 6 — Escrita e Prosa
- Aplicar `.agents/rules/proofreading-protocol.md` integralmente.
- Linguagem é precisa, acadêmica e consistente ao longo do texto?
- Há seções ou parágrafos redundantes que podem ser cortados?

### Lente 7 — Referências e Citações
- Todas as afirmações que requerem citação têm uma?
- Todas as referências no texto aparecem no arquivo `references.bib`?
- Há literatura relevante omitida que o parecerista típico notaria?

---

## Síntese Final

Após as sete lentes, produzir:
1. **Problemas críticos** (aparecem em 3+ lentes): listar e priorizar.
2. **Problemas moderados** (aparecem em 1-2 lentes): listar.
3. **Pontuação de qualidade** usando `.agents/rules/quality-gates.md`.
4. **Próximas ações** ordenadas por impacto.
