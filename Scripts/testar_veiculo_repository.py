
from Repositories.veiculo_repository import VeiculoRepository


repositorio = VeiculoRepository()

try:
    print("=" * 50)
    print("TESTE DO VEICULO REPOSITORY")
    print("=" * 50)

    total = repositorio.contar_documentos()
    print(f"\nTotal de veículos: {total}")

    veiculo = repositorio.buscar_por_id("VEI00001")
    print("\nConsulta por ID:")
    print(veiculo)

    ativos = repositorio.buscar_por_status("ativo")
    print(f"\nVeículos ativos: {len(ativos)}")

    veiculos_linha = repositorio.buscar_por_linha("LIN0001")
    print(f"\nVeículos da linha LIN0001: {len(veiculos_linha)}")

    print("\nTeste concluído!")

finally:
    repositorio.colecao.database.client.close()
