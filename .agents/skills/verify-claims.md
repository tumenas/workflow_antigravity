# Skill: verify-claims

**Descrição:** Chain-of-Verification — rastreia cada afirmação quantitativa do manuscrito até sua fonte nos dados processados e scripts de análise. Garante que nenhum número no texto seja inconsistente com os resultados reais.

**Como invocar:** `verify-claims manuscript/manuscript.qmd`

---

## Protocolo de Verificação

### Passo 1 — Extração de Claims

Ler o manuscrito completo e extrair TODAS as afirmações quantitativas em uma lista:

```
CLAIM #1: [seção, parágrafo] "A média de pressão arterial foi de 120,3 mmHg (DP = 15,1)"
CLAIM #2: [seção, parágrafo] "O coeficiente da variável idade foi β = 0,35 (IC 95%: 0,12–0,58, p < 0,01)"
CLAIM #3: [seção, parágrafo] "A amostra final consistiu de 98 participantes após exclusão de 2 registros inválidos"
...
```

### Passo 2 — Rastreamento para Fonte

Para cada claim, identificar o arquivo de origem:

| Arquivo de Resultado | Contém |
|----------------------|--------|
| `results/tables/tabela_descritiva.csv` | Estatísticas descritivas por grupo |
| `results/tables/coeficientes_regressao.csv` | Coeficientes, ICs e valores p do modelo |
| `results/tables/resultado_regressao.txt` | Sumário completo do modelo |
| `data/processed/dados_processados.csv` | Tamanho amostral após limpeza |

### Passo 3 — Verificação

Para cada claim, comparar o valor no manuscrito com o valor no arquivo fonte:

```
[VERIFICADO ✓] CLAIM #1: média = 120.3 confirmada em tabela_descritiva.csv (linha "pressao_arterial", coluna "mean")
[DISCREPÂNCIA ✗] CLAIM #2: β reportado = 0.35, mas coeficientes_regressao.csv tem 0.352
[VERIFICADO ✓] CLAIM #3: N=98 confirmado — dados_processados.csv tem 98 linhas (excluindo cabeçalho)
```

### Passo 4 — Reporte Final

Produzir:
- **Total de claims verificados**
- **Claims verificados sem problemas**: lista
- **Discrepâncias encontradas**: lista com localização exata e diferença
- **Claims não rastreáveis** (sem arquivo fonte identificável): lista com recomendação

### Regras Importantes

- Arredondar com cuidado: `0.352` pode ser reportado como `0.35` — não é discrepância se o manuscrito especifica casas decimais menores.
- Nunca alterar o manuscrito autonomamente durante esta verificação. Apenas reportar; aguardar instrução do usuário para corrigir.
- Se um claim não puder ser rastreado, reportar como `[NÃO RASTREÁVEL]` e recomendar rodar os scripts novamente.
