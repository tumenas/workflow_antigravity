# Skill: qa-quarto

**Descrição:** Revisão de qualidade adversarial do documento Quarto compilado — verifica layout, referências, figuras, tabelas e consistência entre texto e outputs gerados.

**Como invocar:** `qa-quarto manuscript/manuscript.qmd`

---

## Protocolo

### Pré-requisito

O manuscrito deve ser compilado antes desta revisão:
```powershell
.\run.ps1 paper
```
Se a compilação falhar, corrigir primeiro. Este skill pressupõe um documento compilado com sucesso.

### Checklist de Qualidade

#### 1. Estrutura e Navegação
- [ ] Todas as seções principais estão presentes: Introdução, Metodologia, Resultados, Discussão, Conclusão?
- [ ] A numeração de seções está correta e sequencial?
- [ ] O sumário (TOC), se habilitado, reflete corretamente a estrutura?

#### 2. Figuras
- [ ] Todas as figuras aparecem no documento compilado?
- [ ] Cada figura tem legenda descritiva e completa?
- [ ] As figuras são nítidas (não pixeladas) no PDF/HTML?
- [ ] Todas as referências `@fig-` no texto resolvem corretamente?
- [ ] As figuras estão numeradas sequencialmente (Figura 1, Figura 2...)?

#### 3. Tabelas
- [ ] Todas as tabelas aparecem corretamente formatadas?
- [ ] Cada tabela tem título e nota de rodapé (se aplicável)?
- [ ] Todas as referências `@tbl-` no texto resolvem corretamente?

#### 4. Referências e Citações
- [ ] Nenhuma citação aparece como `[?]` ou `[@chave]` sem resolver?
- [ ] A lista de referências ao final está presente e formatada?
- [ ] Todas as referências citadas no texto aparecem na lista?

#### 5. Equações
- [ ] Equações numeradas são renderizadas corretamente (não como LaTeX cru)?
- [ ] Referências `@eq-` no texto resolvem corretamente?

#### 6. Conteúdo Dinâmico (chunks Python)
- [ ] Todos os chunks de código Python executaram sem erro?
- [ ] Tabelas geradas por código Python aparecem formatadas (não como texto bruto)?
- [ ] Nenhuma célula exibe mensagens de aviso ou traceback?

### Modo Adversarial

Após o checklist, assumir o papel de um leitor crítico:
- "O que neste documento pareceria descuidado ou não-profissional para um parecerista de periódico?"
- Listar até 5 problemas de apresentação que reduziriam a credibilidade do trabalho.

### Reporte Final

Produzir:
- **Itens aprovados**: lista
- **Itens com problemas**: descrição + correção sugerida
- **Pontuação de qualidade de apresentação** (0-100)
