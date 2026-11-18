
from Services.linha_service import LinhaService


servico = LinhaService()

try:
    print("=" * 55)
    print("TESTE DO LINHA SERVICE")
    print("=" * 55)

    indicadores = servico.obter_indicadores_gerais()

    print("\nINDICADORES GERAIS\n")

    for indicador, valor in indicadores.items():
        print(f"{indicador}: {valor}")

    print("\nDISTRIBUIÇÃO POR REGIÃO\n")

    regioes = servico.obter_distribuicao_por_regiao()

    for item in regioes:
        print(f"{item['_id']}: {item['quantidade']}")

    print("\nDISTRIBUIÇÃO POR STATUS\n")

    status = servico.obter_distribuicao_por_status()

    for item in status:
        print(f"{item['_id']}: {item['quantidade']}")

    print("\nTeste concluído!")

finally:
    servico.repositorio.colecao.database.client.close()