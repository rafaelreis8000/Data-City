# DataCity Analytics

## 1. SObre o Projeto

O **DataCity Analytics** é uma aplicação de análise de dados de mobilidade urbana desenvolvida para a cidade fictícia de Nova Esperança, com aproximadamente 750 mil habitantes.

O projeto consiste em investigar problemas relacionados ao atraso nos transportes coletivos, juntamente com a análise da distribuição de passageiros e suas demandas, a duração de cada viagem, as ocorrências operacionais e as avaliações dos usuários.

Dados sintéticos serão utilizados e mapeados no MongoDB em conjunto com Python buscando organizar, tratar, analisar e visualizar dados e informações que apoiem tomadas de decisões e planejamentos acerca do trânsito.

## 2. Objetivo Geral

Desenvolver uma aplicação funcional integrada ao MongoDB capaz de coletar, organizar, preparar, explorar, visualizar e interpretar dados sintéticos de mobilidade urbana, gerando indicadores e recomendações fundamentadas para o planejamento do transporte coletivo de Nova Esperança.

## 3. Objetivos Específicos

- Modelar e organizar os dados de linhas, veículos, viagens e ocorrências;
- Implementar a conexão com o MongoDB utilizando PyMongo;
- Gerar ou importar dados sintéticos reproduzíveis;
- Converter os documentos armazenados em DataFrames com Pandas;
- Utilizar NumPy em operações numéricas de apoio;
- Identificar ausências, duplicidades, inconsistências e valores suspeitos;
- Calcular indicadores de atrasos, duração das viagens, demanda de passageiros e avaliações;
- Produzir gráficos com Matplotlib e interpretar os resultados;
- Exportar tabelas analíticas e elaborar um relatório técnico;
- Propor melhorias para o transporte coletivo com base nas evidências obtidas;
- Documentar o desenvolvimento e os resultados utilizando o método Scrum e os princípios da Programação Orientada a Objetos;

## 4. Tecnologias Utilizadas

| Tecnologia | Finalidade |
| -- | -- |
| Python 3 | Linguagem principal |
| MongoDB | Armazenamento de Dados |
| PyMongo | Integração com o MongoDB |
| Pandas | Manipulação e Análise de Dados |
| NumPy | Operações Numéricas |
| Matplotlib | Construção de gráficos |
| python-dotenv | Configuração de Variáveis de Ambiente |
| Scikit-learn | Agrupamento e Previsão Introdutória |
| Jupyter Notebook | Exploração documentada dos Dados |
| Pytest | Testes Automatizados |

A utilização de uma interface gráfica não faz parte do MVP, mas pode ser integrada futuramente

## 5. Arquitetura da Aplicação

Toda a aplicação será desenvolvida buscando:

- Obter ou gerar dados sintéticos;
- Validar a importação dos dados;
- Armazenar no MongoDB;
- Consultar documentos utilizando o PyMongo;
- Preparar e analisar os dados utilizando Pandas e NumPy;
- Calcular indicadores de mobilidade;
- Gerar gráficos com Matplotlib;
- Exportar os resultados e elaborar recomendações;

## 6. Banco de Dados

O Banco de Dados será salvo como **datacity_db** e deverá conter:

- Linhas: informações sobre as linhas de transporte;
- Veículos: informações sobre os veículos e suas capacidades;
-  Viagens: registros das viagens e suas métricas operacionais;
- Ocorrências: reigstros de eventos associados à operação do transporte;

## 7. Organização e Orientação a Objetos

O código será modular, orientado a objetos e organizado em diferntes pastas para melhor visualização

| Pasta | Finalidade |
| -- | -- |
| Models | Representação das entidades do domínio |
| Config | Configuração e conexão com o  Banco de Dados |
| Repositories | Acesso e consultas ao MongoDB |
| Services | Preparação dos dados e análise de indicadores |
| Visualizations | Criação e salvamento dos gráficos |
| Controllers | Coordenação do fluxo da aplicação |
| Scripts | Validação, geração e importação de dados |

## 8. Metodologia de desenvolvimento

O projeto será modelado seguindo a metodologia ágil Scrum, distribuindo o trabalho em quatro sprints

- Sprint 1: Diagnóstico, arquitetura, organização do projeto e configuração do ambiente;
- Sprint 2: Modelagem documental, validação, importação e consultas no MongoDB;
- Sprint 3: Preparação dos dados, análise exploratória e cálculo de indicadores;
- Sprint 4: Visualizações, testes, relatórios técnicos e apresentação final;

## 9. Indicadores e questões de investigação

Ao processar e analisar a base de dados no MongoDB, deve-se responder essas perguntas:

- Quais linhas e regiões apresentam maiores atrasos médios e medianos?;
- Em quais horários ocorre maior concentração de passageiros?;
- Como a duração e o atraso das viagens variam ao longo do tempo?;
- Quais ocorrências são mais frequentes e em quais regiões?;
- Existe associação entre atrasos e avaliações dos usuários?;
- Há indícios de sobrecarga dos veículos ou distribuição desigual da demanda?;
- Quais três melhorias podem ser recomendadas com base nos resultados?;
- Quais linhas e regiões apresentam os menores atrasos médios e medianos?;
- Quais linhas apresentam o maior desgaste operacional?;
- Quais ações de curto, médio e longo prazo otimizariam o funcionamento das linhas?;

## 10. MVP

Ao final do desenvolvimento, o MVP elaborado deve possuir:

- Código fonte organizado e documentado;
- Conexão funcional com o MongoDB;
- Script de validação e importação dos dados;
- Consultas às quatro coleções obrigatórias;
- Procedimentos de preparação e análise dos dados;
- Tabela analítica exportada em .CSV;
- Notebook Jupyter documentado;
- pelo menos quatro gráficos interpretados;
- Relatório técnico em PDF;
- Diagrama atualizado da arquitetura;
- Apresentação com demonstração funcional da aplicação;

## 11. Qualidade, ética e limitações

Todos os dados utilizados serão sintéticos. O projeto deverá proteger as credenciais de acesso ao banco, evitar dados pessoais reais e documentar as regras de tratamento dos registros.

Atrasos negativos não serão descartados automaticamente, pois podem representar adiantamentos. A avaliação da lotação deverá considerar a capacidade do veículo. As análises também deverão distinguir correlação de causalidade e reconhecer as limitações dos dados sintéticos.

## 12. Configuração e Execução

As instruções completas de instalação, configuração do ambiente virtual, conexão com o MongoDB e execução dos módulos serão documentadas à medida que as funcionalidades forem implementadas.

As credenciais serão configuradas por variáveis de ambiente. O arquivo .env não deverá ser versionado.

**Status do projeto:** estruturação inicial e planejamento. A aplicação será considerada concluída somente após a implementação, os testes e a demonstração dos requisitos obrigatórios.