
from Services.ocorrencia_service import OcorrenciaService


servico = OcorrenciaService()

try:
    print("=" * 55)
    print("TESTE DO OCORRENCIA SERVICE")
    print("=" * 55)

    indicadores = servico.obter_indicadores_gerais()

    print("\nINDICADORES GERAIS\n")

    for indicador, valor in indicadores.items():
        print(f"{indicador}: {valor}")

    print("\nDISTRIBUIÇÃO POR TIPO\n")

    tipos = servico.obter_distribuicao_por_tipo()

    for item in tipos:
        print(f"{item['_id']}: {item['quantidade']}")

    print("\nDISTRIBUIÇÃO POR IMPACTO\n")

    impactos = servico.obter_distribuicao_por_impacto()

    for item in impactos:
        print(f"{item['_id']}: {item['quantidade']}")

    print("\nDISTRIBUIÇÃO POR STATUS\n")

    status = servico.obter_distribuicao_por_status()

    for item in status:
        print(f"{item['_id']}: {item['quantidade']}")

    print("\nTeste concluído!")

finally:
    servico.repositorio.colecao.database.client.close()
