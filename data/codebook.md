# Dicionário de Variáveis (Codebook)

| Variável | Descrição | Fórmula / Definição | Fonte | Unidade |
|---|---|---|---|---|
| `firm_id` | Identificador único da firma | Código numérico / CNPJ / GVKEY | Base Bruta | ID |
| `year` | Ano fiscal | Ano calendário (2016–2023) | Base Bruta | Ano |
| `sector` | Setor econômico | Classificação setorial (CNAE / GICS) | Base Bruta | Categórica |
| `treated` | Grupo de tratamento | 1 se firma afetada pelo choque; 0 caso contrário | Construída | Dummy |
| `post` | Período pós-choque | 1 se `year >= 2020`; 0 caso contrário | Construída | Dummy |
| `did` | Termo de interação DiD | `treated * post` | Construída | Dummy |
| `roa_w` | Retorno sobre Ativos (winsorizado 1%/99%) | Lucro Líquido / Ativo Total | Economatica / CVM | Razão |
| `tobin_q_w` | Q de Tobin (winsorizado 1%/99%) | (Valor de Mercado + Dívida Total) / Ativo Total | Economatica / B3 | Razão |
| `size_w` | Tamanho da firma (winsorizado 1%/99%) | $\ln(\text{Ativo Total})$ | Economatica / CVM | Log |
| `leverage_w` | Alavancagem financeira (winsorizado 1%/99%) | Dívida Total / Ativo Total | Economatica / CVM | Razão |
