# Quality Gates — Critérios de Qualidade para Entregas

## Thresholds

| Pontuação | Gate       | Significado                                           |
|-----------|------------|-------------------------------------------------------|
| 80/100    | Commit     | Satisfatório; pode ser salvo no histórico do Git      |
| 90/100    | Compartilhar | Pronto para revisão de co-autores                   |
| 95/100    | Submissão  | Pronto para envio a periódico científico              |

## Critérios de Avaliação do Manuscrito

Ao avaliar a qualidade de um rascunho, pontuar cada dimensão de 0 a 10:

1. **Clareza da questão de pesquisa** (0-10): A pergunta é precisa, delimitada e relevante?
2. **Revisão de literatura** (0-10): O estado da arte está adequadamente coberto e citado?
3. **Validade interna da metodologia** (0-10): Os métodos respondem à questão de pesquisa proposta?
4. **Qualidade e apresentação dos dados** (0-10): Tabelas e figuras são claras, rotuladas e de alta resolução?
5. **Solidez dos resultados** (0-10): Os achados são coerentes com a metodologia e os dados?
6. **Discussão e contribuição** (0-10): As implicações são discutidas? A contribuição é clara?
7. **Qualidade da escrita** (0-10): Linguagem acadêmica, fluência, ausência de erros?
8. **Integridade das referências** (0-10): Citações no texto correspondem ao BibTeX?
9. **Reprodutibilidade** (0-10): Alguém externo conseguiria reproduzir os resultados a partir do repositório?
10. **Formatação e conformidade** (0-10): O documento segue as diretrizes do periódico-alvo?

**Pontuação total = média das 10 dimensões × 10**

## Critérios de Avaliação de Código Python

1. **Executabilidade**: O script roda do início ao fim sem erros?
2. **Reprodutibilidade**: A semente aleatória (`random_state`, `np.random.seed`) está fixada onde necessário?
3. **Saídas salvas**: Todos os resultados são salvos em disco (não apenas exibidos)?
4. **Documentação**: Cada script tem docstring e comentários nas decisões não-óbvias?
5. **Separação de responsabilidades**: Cada script faz uma coisa (limpeza, análise, plots)?
