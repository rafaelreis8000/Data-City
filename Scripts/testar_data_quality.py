
from Analytics.data_loader import DataFrameLoader
from Analytics.data_quality import DataQuality


loader = DataFrameLoader()
analisador = DataQuality()

try:
    print("=" * 60)
    print("DIAGNOSTICO DE QUALIDADE DOS DADOS")
    print("=" * 60)

    dados = loader.carregar_todos()

    resultados = analisador.diagnosticar_todos(dados)

    for nome, resultado in resultados.items():

        print(f"\nCOLECAO: {nome.upper()}")
        print("-" * 50)

        print(
            f"Total de registros: "
            f"{resultado['total_registros']}"
        )

        print(
            f"Total de colunas: "
            f"{resultado['total_colunas']}"
        )

        print(
            f"Registros duplicados: "
            f"{resultado['registros_duplicados']}"
        )

        print(
            f"IDs duplicados: "
            f"{resultado['ids_duplicados']}"
        )

        print("\nDiagnóstico por coluna:")

        print(resultado["diagnostico_colunas"])

    print("\nDiagnóstico concluído!")

finally:
    loader.fechar_conexao()