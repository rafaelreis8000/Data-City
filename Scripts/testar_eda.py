
from Analytics.data_loader import DataFrameLoader
from Analytics.data_cleaner import DataCleaner
from Analytics.eda import ExploratoryAnalysis


loader = DataFrameLoader()
limpador = DataCleaner()
analise = ExploratoryAnalysis()

try:
    dados = loader.carregar_todos()

    dados_limpos = limpador.limpar_todos(dados)

    print("=" * 60)
    print("ANALISE EXPLORATORIA DE DADOS")
    print("=" * 60)

    # Análise geral das viagens
    resultado_viagens = analise.analisar_viagens(
        dados_limpos["viagens"]
    )

    print("\nINDICADORES GERAIS DAS VIAGENS")
    print("-" * 50)

    for indicador, valor in resultado_viagens.items():
        print(f"{indicador}: {valor}")

    # Análise das viagens por linha
    resultado_linhas = analise.analisar_viagens_por_linha(
        dados_limpos["viagens"]
    )

    print("\nDESEMPENHO DAS LINHAS")
    print("-" * 50)

    print(resultado_linhas.head(10).to_string(index=False))

    # Análise das ocorrências
    resultado_ocorrencias = analise.analisar_ocorrencias(
        dados_limpos["ocorrencias"]
    )

    print("\nOCORRENCIAS POR TIPO")
    print(resultado_ocorrencias["ocorrencias_por_tipo"])

    print("\nOCORRENCIAS POR NIVEL DE IMPACTO")
    print(resultado_ocorrencias["ocorrencias_por_impacto"])

    print("\nOCORRENCIAS POR STATUS")
    print(resultado_ocorrencias["ocorrencias_por_status"])

    print("\nAnalise exploratoria concluida!")

finally:
    loader.fechar_conexao()