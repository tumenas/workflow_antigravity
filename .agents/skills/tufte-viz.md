# Skill: tufte-viz

**Descrição:** Ideação e crítica de visualizações de dados com base nos princípios clássicos de Edward Tufte (*The Visual Display of Quantitative Information*, *Envisioning Information* e *Beautiful Evidence*). Foca na maximização do *data-ink ratio*, na eliminação de *chartjunk*, na integridade gráfica, no cálculo do *lie factor*, no uso de múltiplos pequenos (*small multiples*) e na alta densidade de informação integrada.

**Como invocar:** 
- Para analisar uma visualização existente (código ou imagem): `tufte-viz analysis/03_plots.py` ou `tufte-viz results/figures/grafico.png`
- Para planejar uma nova visualização: `tufte-viz` indicando os dados disponíveis, o objetivo de comparação e a história que deseja contar.

---

## Fluxo de Trabalho

### Modo 1: Planejamento de Nova Visualização (Ideação)

1. **Clarificar a História dos Dados:**
   - Quais comparações são de fato de interesse científico?
   - Qual é o insight central que o leitor deve obter em poucos segundos?
   - Quem é o público-alvo (revisores, público geral, comunidade especializada)?

2. **Selecionar a Abordagem (Tipos de Gráficos e Layouts):**
   - **Muitas comparações cruzadas:** Preferir múltiplos pequenos (*small multiples*) a gráficos de linhas múltiplos complexos ou barras empilhadas que dificultam a leitura rápida.
   - **Alta densidade de dados:** Considerar tabelas de dados ricas, gráficos de dispersão com *rug plots*, ou *sparklines* integrados diretamente ao texto.
   - **Séries temporais:** Gráficos de linhas limpos, com grades ausentes ou extremamente sutis (cinza claro, pontilhado, recuadas).
   - **Proporções (Part-to-Whole):** Evitar gráficos de pizza (*pie charts*); usar barras horizontais ordenadas ou tabelas limpas para maior legibilidade.

3. **Desenho focado em Tinta de Dados (Data-Ink):**
   - Começar com o mínimo absoluto. Cada elemento visual deve justificar sua presença.
   - Usar escala de cinza por padrão. Reservar cor exclusivamente para destacar dados de interesse ou diferenciar categorias importantes (nunca para decoração).

---

### Modo 2: Crítica de Visualização Existente (Review)

1. **Calcular a Integridade Gráfica:**
   - **Fator de Mentira (Lie Factor):**
     $$Lie Factor = \frac{\text{Tamanho do efeito mostrado no gráfico}}{\text{Tamanho do efeito real nos dados}}$$
     O *Lie Factor* deve ser o mais próximo possível de 1.0. Se for significativamente diferente, apontar distorções nas escalas, eixos truncados ou efeito 3D artificial.
   - Garantir que a escala vertical comece do zero em gráficos de barras. Em gráficos de linhas/dispersão, focar no intervalo relevante, mas sinalizar claramente os limites dos eixos.

2. **Identificar Lixo Gráfico (Chartjunk):**
   - Elementos decorativos vazios, preenchimentos gradientes desnecessários, bordas pesadas de plotagem.
   - Linhas de grade grossas e escuras (que competem com a linha do dado).
   - Efeitos 3D desprovidos de informação tridimensional real.
   - Texturas de preenchimento complexas (que causam efeitos de tremulação/Moiré).

3. **Avaliar a Proporção de Tinta de Dados (Data-Ink Ratio):**
   - Identificar o que pode ser apagado ou simplificado sem perda de informação útil.
   - Apontar redundâncias (ex: legenda duplicando rótulos diretos nas séries de dados, valores escritos repetidamente ao lado de pontos já escalados).

4. **Propor Melhorias Práticas:**
   - Fornecer sugestões de alteração no código de plotagem (ex: substituições no `matplotlib`, `seaborn` ou `ggplot2`).

---

## Testes de Validação Pré-Publicação

Antes de aprovar qualquer gráfico, o assistente deve submetê-lo a dois testes críticos:

### A. Teste do Apagador (The Eraser Test)
Para cada elemento da figura (rótulos, eixos, linhas de grade, bordas, anotações):
- *Pergunta:* Se este elemento for apagado, perde-se alguma informação essencial que não esteja expressa de outra forma?
- Se a resposta for "Não", o elemento deve ser removido ou suavizado.
- **Exemplo de correção:** Substituir a moldura retangular pesada do gráfico por um *range-frame* (eixos que terminam exatamente no valor mínimo e máximo dos dados reais).

### B. Teste de Colisão (The Collision Test)
Para cada elemento de texto no gráfico (rótulos de dados, anotações, notas explicativas, títulos de eixos):
- Desenhar mentalmente uma caixa delimitadora (*bounding box*) ao redor do texto.
- *Pergunta:* Algum outro elemento (linha de dados, ponto, grade ou outro texto) invade ou colide com essa caixa?
- Se sim, resolver o conflito: afastar o rótulo, usar uma linha de chamada (*leader line*) sutil, ou mover o texto explicativo para a legenda externa (*caption*) da figura.

---

## Referência de Princípios Clássicos de Tufte

- **Proporção de Tinta de Dados (Data-Ink Ratio):**
  $$\text{Data-Ink Ratio} = \frac{\text{Tinta de dados (elementos que mudam se os dados mudarem)}}{\text{Tinta total gasta no gráfico}}$$
  *Objetivo:* Maximizar esta proporção. Apague tinta que não carrega informação.
  
- **Múltiplos Pequenos (Small Multiples):**
  Série de gráficos em miniatura dispostos em uma grade, compartilhando a mesma escala e formato. Permite comparação visual direta e rápida de diferentes categorias, variáveis ou fatias temporais sem sobrecarregar um único plano.

- **Integração de Texto e Gráfico:**
  Palavras, números e imagens devem ser integrados harmonicamente no mesmo plano visual. Evite forçar o leitor a saltar constantemente entre o gráfico e uma legenda distante para decodificar os símbolos (prefira rotular as séries de dados diretamente no final de cada linha).

- **Detalhe Micro/Macro:**
  O design gráfico deve permitir leitura em múltiplos níveis de detalhe: uma visão macro geral (para compreender o padrão principal) e uma visão micro detalhada (para ler valores e outliers específicos ao olhar de perto).

---

## Checklist de Avaliação Rápida

- [ ] **Lie Factor ≈ 1.0** (sem distorção visual)
- [ ] **Maximização da proporção de tinta de dados** (data-ink ratio)
- [ ] **Zero lixo gráfico** (chartjunk removido)
- [ ] **Identificação e rotulação clara** de eixos e variáveis
- [ ] **Responde à pergunta "Comparado a quê?"**
- [ ] **Mostra causalidade** ou mecanismos onde for relevante
- [ ] **Multivariado** (evita redução excessiva de variáveis importantes)
- [ ] **Textos, números e imagens integrados** harmonicamente
- [ ] **Revela múltiplos níveis de detalhe** (micro + macro)
- [ ] **Camadas claras:** dados primários em destaque, informações secundárias recuadas
- [ ] **Densidade de dados apropriada**
