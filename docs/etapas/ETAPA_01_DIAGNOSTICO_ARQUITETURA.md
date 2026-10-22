# Etapa 01 - Diagnóstico e Arquitetura

## 1. Objetivo

Compreender o problema de mobilidade urbana apresentado no estudo de caso e definir a arquitetura inicial do DataCity Analytics.

## 2. Diagnóstico do problema

A cidade fictícia de Nova Esperança possui aproximadamente 750 mil habitantes e enfrenta desafios relacionados à operação do transporte coletivo.

O projeto pretende analisar dados de linhas, veículos, viagens e ocorrências para identificar padrões de atraso, distribuição da demanda, duração das viagens e possíveis problemas operacionais.

Os resultados deverão apoiar recomendações fundamentadas nos dados disponíveis, sem presumir relações de causa e efeito que não tenham sido demonstradas.

## 3. Objetivos da Análise

- Identificar linhas e regiões com maiores atrasos;
- Investigar os horários de maior concentração de passageiros;
- Analisar a duração das viagens e sua variação ao longo do tempo;
- Identificar as ocorrências operacionais mais frequentes;
- Investigar a associação entre atrasos e avaliações dos usuários;
- Avaliar indícios de sobrecarga considerando a capacidade de cada veículo;
- Elaborar recomendações com base nos resultados;

## 4. Requisitos Funcionais

- Conexão com o MongoDB;
- Consultar as coleções obrigatórias;
- Validar e preparar os dados;
- Calcular indicadores de mobilidade;
- Gerar pelo menos quatro gráficos para análise;
- Exportar tabelas analíticas em CSV;
- Produzir um notebook Jupyter e um relatório técnico em PDF;

## 5. Requisitos não funcionais

- Código organizado em módulos e classes;
- Configurações e credenciais mantidas fora do código-fonte;
- Tratamento de erros de conexão e inconsistência nos dados;
- Testes para funcionalidades críticas;
- Documentação atualizada durante o desenvolvimento;
- Resultados reproduzíveis sempre que possível;

## 6. Arquitetura proposta

A aplicação será organizada nas seguintes camadas:

- Models: representação das entidades do domínio;
- Config: configurações e conexão com o MongoDB;
- Repositories: consultas e operações de acesso aos dados;
- Services: validação, preparação, análise e cálculo de indicadores;
- Visualizations: criação e salvamento dos gráficos;
- Controllers: coordenação dos casos de uso;
- Scripts: geração, validação e importação dos dados;

### Fluxo Geral

Dados JSON > Validação e importação > MongoDB > Repositories > Services > Pandas e NUmPy > Indicadores e gráficos > CSV e relatório técnico.

## 7. Coleções do MongoDB

O banco de dados será denominado datacity_db e deverá conter:

- Linhas;
- Veículos;
- Viagens;
- Ocorrências;

Antes da importação, os arquivos de origem deverão ser inspecionados para confirmar seus campos, tipos, relacionamentos e quantidade de registros.

## 8. Decisões e cuidados

- Utilizar dados sintéticos e registrar sua origem;
- Evitar duplicações durante importações repetidas;
- Não descartar atrasos negativos sem investigar seu significado;
- Considerar a capacidade do veículo ao avaliar lotação;
- Evitar contar a mesma viagem mais de uma vez ao relacioná-la com ocorrências;
- Documentar as regras de tratamento dos dados;
- Não interpretar correlação como causalidade;

## 9. Critérios

- [ ] O problema estiver documentado;
- [ ] Os requisitos funcionais e não funcionais estiverem definidos;
- [ ] A arquitetura inicial estiver registrada;
- [ ] As quatro coleções obrigatórias estiverem identificadas;
- [ ] Os principais cuidados com a qualidade dos dados estiverem documentados;
- [ ] As decisões estiverem alinhadas ao estudo de caso;