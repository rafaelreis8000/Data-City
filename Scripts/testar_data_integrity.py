
from Analytics.data_loader import DataFrameLoader
from Analytics.data_integrity import DataIntegrity


loader = DataFrameLoader()
analisador = DataIntegrity()

try:
    print("=" * 60)
    print("VERIFICACAO DE INTEGRIDADE REFERENCIAL")
    print("=" * 60)

    dados = loader.carregar_todos()

    resultados = analisador.verificar_todos(dados)

    for nome, resultado in resultados.items():

        print(f"\nRELACIONAMENTO: {nome}")
        print("-" * 50)

        print(
            f"Total de referencias: "
            f"{resultado['total_referencias']}"
        )

        print(
            f"Referencias nulas: "
            f"{resultado['referencias_nulas']}"
        )

        print(
            f"Referencias invalidas: "
            f"{resultado['referencias_invalidas']}"
        )

        if resultado["exemplos_invalidos"]:
            print(
                f"Exemplos invalidos: "
                f"{resultado['exemplos_invalidos']}"
            )

    print("\nVerificacao concluida!")

finally:
    loader.fechar_conexao()