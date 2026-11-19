
from Analytics.data_loader import DataFrameLoader


loader = DataFrameLoader()

try:
    print("=" * 60)
    print("TESTE DE INTEGRACAO COM PANDAS")
    print("=" * 60)

    dados = loader.carregar_todos()

    for nome, dataframe in dados.items():

        print(f"\nCOLECAO: {nome.upper()}")
        print("-" * 45)

        print(f"Quantidade de registros: {len(dataframe)}")
        print(f"Quantidade de colunas: {len(dataframe.columns)}")

        print("\nPrimeiros registros:")
        print(dataframe.head(3))

    print("\n" + "=" * 60)
    print("INTEGRACAO CONCLUIDA!")
    print("=" * 60)

finally:
    loader.fechar_conexao()