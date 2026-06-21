# Verification Protocol — Verificação Final de Execução

## Objetivo

Protocolo leve de verificação de sanidade a ser executado ao final de qualquer tarefa, antes de declarar conclusão.

## Os 5 Pontos de Verificação

### 1. Outputs Existem
Confirmar que todos os arquivos de saída esperados pela tarefa foram criados e não estão vazios.

```
Verificar: [ ] arquivo gerado existe? [ ] tamanho > 0 bytes?
```

### 2. Nenhum Erro Silencioso
Scripts Python e R podem terminar sem lançar exceção mesmo produzindo resultados errados. Verificar:
- O output faz sentido semanticamente? (ex: uma média de pressão arterial de 120 mmHg é plausível; 1200 mmHg não é)
- O número de linhas/registros no output é coerente com o input?

### 3. Consistência com o Manuscrito
Se a tarefa alterou qualquer resultado numérico, verificar se o manuscrito `manuscript/manuscript.qmd` ainda está sincronizado:
- Tabelas dinâmicas no `.qmd` referenciam os arquivos corretos?
- Figuras referenciadas existem em `results/figures/`?

### 4. Reprodutibilidade a Frio
A tarefa produz o mesmo resultado se executada por um terceiro partindo do zero?
- Todos os inputs estão disponíveis em `data/raw/` ou `data/processed/`?
- Todas as dependências estão em `requirements.txt`?
- Nenhum caminho absoluto ou arquivo local está hardcoded?

### 5. Registro de Aprendizados
Se durante a execução foi descoberto algo novo (um bug, uma convenção, um comportamento inesperado):
- Adicionar `[LEARN:categoria] descrição` em `.agents/MEMORY.md`.

## Declaração de Conclusão

Só declarar uma tarefa concluída após passar pelos 5 pontos acima. Se qualquer ponto falhar, corrigir primeiro.
