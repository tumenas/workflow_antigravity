# Skill: review-paper

**Descrição:** Revisão científica completa de um manuscrito acadêmico. Suporta três modos: revisão única (padrão), loop adversarial crítico-corretor, e simulação de revisão por pares calibrada a um periódico-alvo.

**Como invocar:** Informe o caminho do manuscrito e o modo desejado.
- Modo padrão: `review-paper manuscript/manuscript.qmd`
- Modo adversarial: `review-paper manuscript/manuscript.qmd --adversarial`
- Modo peer review: `review-paper manuscript/manuscript.qmd --peer [nome do periódico]`

---

## Modo Padrão (Single-Pass)

Produzir um relatório de revisão completo e construtivo — do tipo que um parecerista de periódico top escreveria.

### Estrutura do Relatório

**1. Avaliação Geral**
- Qual é a contribuição central do artigo?
- Está dentro do escopo do periódico-alvo?
- Recomendação preliminar: Accept / Minor Revision / Major Revision / Reject

**2. Pontos Fortes** (liste no mínimo 3)

**3. Problemas Maiores** (que comprometeriam a aceitação)
Para cada problema: descrever o problema, indicar onde aparece, sugerir como resolver.

**4. Problemas Menores** (que devem ser corrigidos mas não comprometem aceitação)

**5. Questões de Reprodutibilidade**
- Os scripts em `analysis/` reproduzem os resultados reportados?
- Os dados estão disponíveis ou documentados?
- Aplicar o protocolo em `.antigravitycli/rules/cross-artifact-review.md`.

**6. Qualidade da Escrita**
- Aplicar `.antigravitycli/rules/proofreading-protocol.md` nos primeiros 3 parágrafos de cada seção.

**7. Pontuação de Qualidade**
- Pontuar as 10 dimensões de `.antigravitycli/rules/quality-gates.md`.
- Reportar pontuação total e justificar dimensões abaixo de 7.

**8. Próximas Ações Prioritárias** (lista numerada e ordenada por impacto)

---

## Modo Adversarial (`--adversarial`)

Loop iterativo crítico-corretor (máximo 5 rodadas):

1. **Crítico**: Identifica os 3 problemas mais graves do manuscrito.
2. **Corretor**: Propõe e aplica edições para cada problema (com aprovação do usuário).
3. **Crítico**: Re-avalia o manuscrito corrigido.
4. Repetir até APROVADO ou 5 rodadas.

---

## Modo Peer Review (`--peer [periódico]`)

Pipeline editorial simulada: **desk review do editor → seleção de pareceristas → 2 pareceristas cegos com disposições diferentes → síntese editorial**.

Disposições dos pareceristas (amostradas aleatoriamente):
- **STRUCTURAL**: foco em coerência lógica e estrutura argumentativa
- **CREDIBILITY**: foco em validade interna e robustez dos resultados
- **MEASUREMENT**: foco em operacionalização e qualidade dos dados
- **POLICY**: foco em relevância e implicações práticas
- **THEORY**: foco em contribuição teórica e revisão de literatura
- **SKEPTIC**: postura crítica — busca razões para rejeitar

Salvar relatórios em `quality_reports/peer_review_[manuscrito]/`.
