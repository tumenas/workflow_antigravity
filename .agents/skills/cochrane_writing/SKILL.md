---
name: cochrane-writing
description: Academic writing guidelines and automated auditing based on John H. Cochrane's Writing Tips for Ph.D. Students
workflow_stage: writing
compatibility:
  - claude-code
  - cursor
  - gemini-cli
author: Antigravity Agent
version: 1.0.0
tags:
  - academic-writing
  - economics
  - paper-writing
  - style-guide
---

# Skill: cochrane_writing

**Descrição:** Orientação e auditoria de redação acadêmica baseadas no guia *"Writing Tips for Ph.D. Students"* do economista John H. Cochrane. Ajuda a estruturar artigos científicos (especialmente em economia e finanças), refinar a prosa (voz ativa, clareza, concisão) e garantir a solidez metodológica da estratégia de identificação empírica.

**Como invocar:** `cochrane_writing manuscript/manuscript.qmd`

---

## 1. Princípios de Organização

John Cochrane defende um estilo **triangular** ou **jornalístico** de escrita científica, em oposição ao estilo "romance de mistério" ou "piada" (onde o resultado só aparece no final).

### Abstract (100–150 palavras)
- Deve resumir a **contribuição central e inédita** em termos concretos.
- Diga o que você encontrou, não o que você procurou (evite *"dados são analisados, testes são feitos"*).
- Não cite literatura no abstract.

### Introdução (Máximo 3 páginas)
- Comece imediatamente com a pergunta de pesquisa e a contribuição principal.
- Apresente fatos e números concretos (ex: *"Em uma regressão de X sobre Y, controlando por Z, o coeficiente é Q"*), não apenas conclusões vagas (ex: *"Rejeitamos a teoria X"*).
- **Evite "limpar a garganta"**: não inicie com frases filosóficas, discussões sobre a importância histórica do assunto ou longas motivações de políticas públicas.
- O parágrafo de "roadmap" (*"A Seção 2 apresenta o modelo..."*) é opcional e consome espaço valioso.

### Revisão de Literatura
- **Não inicie a introdução** com páginas de revisão bibliográfica.
- Coloque a revisão em uma seção separada ou parágrafo delimitado após a introdução.
- Foque em contrastar seu trabalho com os **2 ou 3 artigos mais próximos**. Seja generoso e preciso nas citações.

### Corpo do Artigo e Teoria
- **Regra de Ouro**: Nada deve vir antes do resultado principal que o leitor não precise saber para entendê-lo.
- **Teoria**: Use o mínimo necessário para fundamentar a análise empírica. Não escreva um modelo geral se no trabalho empírico você usará uma versão simplificada (escreva direto a versão especializada).
- **Trabalho Empírico**: Comece direto pelo resultado principal. Evite exercícios de aquecimento, descrições exaustivas de dados conhecidos ou estimativas preliminares.

### Conclusão e Apêndices
- Mantenha a conclusão curta. Não repita todos os seus resultados. Aponte limitações reais, implicações e rumos futuros.
- Use apêndices (especialmente apêndices online) para colocar discussões de literatura secundárias, generalizações de modelos e dezenas de testes de robustez.

---

## 2. Diretrizes de Escrita e Estilo de Prosa

### Voz Ativa vs. Passiva
- Use preferencialmente a **voz ativa** (ex: *"I estimate..."* ou *"Table 5 presents..."*).
- Evite construções passivas que mascaram a responsabilidade da decisão metodológica (ex: *"It is assumed that..."*, *"Data were constructed..."*).
- Em artigos individuais, use **"I"** (Eu) em vez do plural majestático **"We"** (Nós). Use "we" apenas em coautorias ou para se referir a "você (leitor) e eu".

### Precisão e Vocabulário
- Evite jargões técnicos desnecessários e adjetivos de autoelogio (*"striking results"*, *"very significant"*, *"very novel"*). Se o trabalho for bom, o leitor dará os adjetivos.
- Use palavras curtas e simples: prefira **"use"** a *"utilize"*, **"several"** a *"diverse"*.
- **Elimine rodeios antes do "que" (that)**: remova expressões como *"It should be noted that..."*, *"It is easy to show that..."*. Apenas faça a afirmação direta.
- **Clothe the naked "this"**: sempre acompanhe a palavra "this" por um substantivo substantivado (ex: *"this regression shows"*, *"this estimation implies"*, em vez de apenas *"this shows"*).
- Evite abreviações de nomes de autores (escreva *"Fama and French"*, não *"FF"*).
- "Where" refere-se a um local físico. Para modelos, equações ou contextos teóricos, use **"in which"** (ex: *"models in which consumers have..."*).

### Tabelas e Figuras
- **Legendas Auto-suficientes**: Um leitor que passa os olhos deve entender a tabela/figura sem precisar ler o texto (inclua a equação estimada, definição de variáveis e a variável dependente).
- Não coloque números em tabelas que não sejam discutidos no texto.
- **Precisão Numérica**: Use de **2 a 3 dígitos significativos** no máximo. Exiba coeficientes e erros padrão de forma limpa (ex: `4.6` com erro de `0.7`, não `4.56783` com `0.6789`).
- Use unidades sensíveis (ex: porcentagens) para facilitar a leitura.

---

## 3. Checklist de Identificação Empírica

Toda análise empírica deve responder com clareza a 6 perguntas fundamentais de identificação:

1. **Origem da Variabilidade**: Qual mecanismo econômico causou a dispersão na variável independente ($X$)?
2. **Natureza do Erro**: Qual mecanismo econômico constitui o termo de erro? O que mais afeta $Y$ além de $X$?
3. **Exogeneidade**: Por que o termo de erro não é correlacionado com a variável de interesse ($X$) em termos econômicos?
4. **Validade de Instrumentos (se aplicável)**: Por que os instrumentos correlacionam-se com $X$ e são exógenos em relação ao erro?
5. **Controle vs. Instrumento**: A variável $Z$ deve ser usada como controle na especificação ou como instrumento para $X$?
6. **Fonte de Variação**: Qual variação nos dados está direcionando as estimativas? (Ex: com efeito fixo de firma, a variação é *intra-firma ao longo do tempo*; sem efeito fixo, é *entre firmas*).

---

## 4. Auditoria Automatizada (Linter Cochrane)

Este skill inclui um script Python (`scripts/audit_cochrane.py`) para analisar rascunhos em `.qmd` ou `.tex` e apontar desvios das diretrizes de Cochrane.

### Como Executar a Auditoria:
```powershell
python .agents/skills/cochrane_writing/scripts/audit_cochrane.py manuscript/manuscript.qmd
```
O script exibirá avisos com o número da linha, o trecho problemático e a sugestão de correção com base nas regras de John Cochrane.
