from Analytics.data_loader import DataFrameLoader
from Analytics.relationship_quality import RelationshipQuality


loader = DataFrameLoader()
analisador = RelationshipQuality()

try:
    print("=" * 70)
    print("DIAGNOSTICO DE INTEGRIDADE DOS RELACIONAMENTOS")
    print("=" * 70)

    dados = loader.carregar_todos()

    resultados = analisador.diagnosticar_relacionamentos(dados)

    for relacionamento, resultado in resultados.items():

        print(f"\n{relacionamento}")
        print("-" * 60)

        print(
            f"Total de referencias: "
            f"{resultado['total_referencias']}"
        )

        print(
            f"Referencias nulas: "
            f"{resultado['referencias_nulas']}"
        )

        print(
            f"Referencias validas: "
            f"{resultado['referencias_validas']}"
        )

        print(
            f"Referencias invalidas: "
            f"{resultado['referencias_invalidas']}"
        )

    print("\nDiagnostico concluido!")

finally:
    loader.fechar_conexao()