
from Analytics.data_loader import DataFrameLoader
from Analytics.data_cleaner import DataCleaner
from Analytics.visualizations import DataVisualization


loader = DataFrameLoader()
limpador = DataCleaner()
visualizador = DataVisualization()

try:
    print("=" * 60)
    print("GERACAO DE GRAFICOS")
    print("=" * 60)

    dados = loader.carregar_todos()

    dados_limpos = limpador.limpar_todos(dados)

    visualizador.gerar_todos(dados_limpos)

    print("\nGraficos gerados com sucesso!")

    print("\nArquivos salvos em:")
    print("outputs/graficos/")

finally:
    loader.fechar_conexao()