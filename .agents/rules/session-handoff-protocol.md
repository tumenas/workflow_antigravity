# Session Handoff Protocol — Protocolo de Continuidade de Sessão

## Objetivo
Garantir a continuidade do trabalho entre sessões, minimizando o consumo de tokens e evitando a repetição de análises ou pesquisas já realizadas.

## No Início da Sessão (Check-in)
1. **Verificar Estado:** Antes de qualquer ação, verificar se existe o arquivo `quality_reports/session_logs/SESSION_STATE.md`.
2. **Carregar Contexto:** Se o arquivo existir, ler seu conteúdo para entender onde o trabalho parou, quais decisões foram tomadas e quais são os próximos passos imediatos.
3. **Resumo de Partida:** Iniciar a sessão confirmando ao usuário que o estado anterior foi carregado: "Estado da sessão anterior carregado. Paramos em [PONTO X], o plano atual é [PLANO Y]."

## No Final da Sessão (Check-out)
Antes de encerrar a interação (especialmente em tarefas longas ou complexas), o agente **deve** atualizar ou criar o arquivo `quality_reports/session_logs/SESSION_STATE.md` com as seguintes seções:

### 1. Status do Projeto
- **O que foi feito:** Lista concisa de tarefas concluídas nesta sessão.
- **O que falta:** Lista do que ainda precisa ser executado.
- **Bloqueios:** Obstáculos encontrados ou dependências pendentes.

### 2. Base de Conhecimento Local
- **Decisões Tomadas:** Por que escolhemos o modelo X em vez do Y? Qual critério de limpeza foi aplicado?
- **Descobertas:** Insights importantes sobre os dados ou sobre a estrutura do projeto.

### 3. Próximos Passos Imediatos
- Lista de 2-3 comandos ou ações que devem ser executados assim que a próxima sessão começar.

## Regras de Manutenção
- O arquivo deve ser **curto e direto**.
- Não deve conter logs de erros extensos ou códigos completos (para isso existem os logs de execução e os próprios scripts).
- Deve ser sobrescrito a cada encerramento de sessão produtiva para manter apenas o estado mais recente.
