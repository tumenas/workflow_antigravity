# Skill: research-ideation

**Descrição:** Brainstorming estruturado de questões de pesquisa, especificações de modelos, estratégias de identificação e verificações de robustez para um projeto acadêmico em desenvolvimento.

**Como invocar:** `research-ideation [descrição breve do projeto ou dado disponível]`

---

## Protocolo

### Fase 1 — Diagnóstico do Projeto

Fazer ao usuário (se ainda não respondido):
1. Qual é o fenômeno que você quer estudar?
2. Qual é a variável dependente de interesse?
3. Quais dados você tem disponíveis? (fonte, período, unidade de análise)
4. Qual é o mecanismo causal que você hipotetiza?
5. Há algum resultado esperado ou surpreendente nos dados preliminares?

### Fase 2 — Questões de Pesquisa

Propor 3 versões da questão de pesquisa com diferentes graus de ambição:
- **Versão conservadora**: descritiva/exploratória — o que observamos?
- **Versão moderada**: associação — X está associado a Y controlando por Z?
- **Versão ambiciosa**: causal — X causa Y? Qual é o mecanismo?

### Fase 3 — Especificações do Modelo

Para cada questão, propor:
- Modelo baseline
- Covariáveis de controle sugeridas (com justificativa)
- Possíveis problemas de endogeneidade
- Estratégias de identificação (se causal)

### Fase 4 — Análises de Robustez

Propor verificações de robustez para os achados principais:
1. Especificações alternativas do modelo
2. Subamostras (ex: por grupo, período, região)
3. Medidas alternativas para variáveis principais
4. Testes de sensibilidade (ex: inclusão/exclusão de outliers)

### Fase 5 — Posicionamento na Literatura

- Qual é o artigo mais próximo do que você está propondo?
- Em que o seu artigo se diferencia?
- Qual é a contribuição marginal para a literatura?
