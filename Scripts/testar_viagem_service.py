
from Services.viagem_service import ViagemService


servico = ViagemService()

try:
    print("=" * 55)
    print("TESTE DO VIAGEM SERVICE")
    print("=" * 55)

    indicadores = servico.obter_indicadores_gerais()

    print("\nINDICADORES GERAIS DE VIAGENS\n")

    for indicador, valor in indicadores.items():
        print(f"{indicador}: {valor}")

    print("\nTeste concluído!")

finally:
    servico.repositorio.colecao.database.client.close()
