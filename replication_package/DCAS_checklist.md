# DCAS (Data and Code Availability Standard) Checklist

- [ ] Data Availability Statement presente no artigo e no README.
- [ ] Todas as bases de dados possuem fonte, data de acesso e licença documentadas.
- [ ] Script mestre (`src/00_master.py`) executa toda a pipeline em um único comando.
- [ ] Requisitos computacionais (versão do Python/R/Stata, pacotes, tempo de execução) documentados.
- [ ] Cada Tabela e Figura do artigo está mapeada ao script exato que a gera.
- [ ] Nenhum caminho absoluto (ex.: `C:\Users\...`) presente nos scripts.
- [ ] Sementes aleatórias (`np.random.seed`) fixadas em todas as etapas estocásticas.
- [ ] Dados restritos/proprietários não foram incluídos no pacote (substituídos por `access_restricted_data.md`).
