
from Analytics.data_loader import DataFrameLoader
from Analytics.data_cleaner import DataCleaner


loader = DataFrameLoader()
limpador = DataCleaner()

try:
    print("=" * 60)
    print("PREPARACAO DOS DADOS")
    print("=" * 60)

    dados = loader.carregar_todos()

    dados_limpos = limpador.limpar_todos(dados)

    for nome, dataframe in dados_limpos.items():

        print(f"\nCOLECAO: {nome.upper()}")
        print("-" * 50)

        print(f"Registros originais: {len(dados[nome])}")
        print(f"Registros preparados: {len(dataframe)}")

        print(
            "Quantidade de colunas:",
            len(dataframe.columns)
        )

        print(
            "DataFrame preparado:",
            "Sim" if isinstance(dataframe, type(dados[nome]))
            else "Nao"
        )

    print("\nPreparacao concluida!")

finally:
    loader.fechar_conexao()