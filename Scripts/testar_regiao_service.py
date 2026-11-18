
from Services.regiao_service import RegiaoService


servico = RegiaoService()

try:
    print("=" * 55)
    print("TESTE DO REGIAO SERVICE")
    print("=" * 55)

    indicadores = servico.obter_indicadores_gerais()

    print("\nINDICADORES GERAIS\n")

    for indicador, valor in indicadores.items():
        print(f"{indicador}: {valor}")

    print("\nDISTRIBUIÇÃO POR ZONA\n")

    zonas = servico.obter_distribuicao_por_zona()

    for item in zonas:
        print(f"\nZona: {item['_id']}")
        print(f"Regiões: {item['quantidade_regioes']}")
        print(f"População estimada: {item['populacao_estimada']}")
        print(f"Área total: {item['area_total_km2']} km²")

    print("\nTESTE DE BUSCA POR ZONA\n")

    regioes_centro = servico.buscar_regioes_por_zona("Centro")

    print(f"Regiões encontradas na zona Centro: {len(regioes_centro)}")

    print("\nTeste concluído!")

finally:
    servico.repositorio.colecao.database.client.close()