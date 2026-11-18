
from Services.veiculo_service import VeiculoService


servico = VeiculoService()

try:
    print("=" * 55)
    print("TESTE DO VEICULO SERVICE")
    print("=" * 55)

    indicadores = servico.obter_indicadores_gerais()

    print("\nINDICADORES GERAIS\n")

    for indicador, valor in indicadores.items():
        print(f"{indicador}: {valor}")

    print("\nDISTRIBUIÇÃO POR COMBUSTÍVEL\n")

    combustiveis = servico.obter_distribuicao_por_combustivel()

    for item in combustiveis:
        print(f"{item['_id']}: {item['quantidade']}")

    print("\nDISTRIBUIÇÃO POR STATUS\n")

    status = servico.obter_distribuicao_por_status()

    for item in status:
        print(f"{item['_id']}: {item['quantidade']}")

    print("\nTeste concluído!")

finally:
    servico.repositorio.colecao.database.client.close()
