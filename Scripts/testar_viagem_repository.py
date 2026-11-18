
from Repositories.viagem_repository import ViagemRepository


repositorio = ViagemRepository()

try:
    print("=" * 50)
    print("TESTE DO VIAGEM REPOSITORY")
    print("=" * 50)

    total = repositorio.contar_documentos()
    print(f"\nTotal de viagens: {total}")

    viagem = repositorio.buscar_por_id("VIA000001")
    print("\nConsulta por ID:")
    print(viagem)

    viagens_linha = repositorio.buscar_por_linha("LIN0143")
    print(f"\nViagens da linha LIN0143: {len(viagens_linha)}")

    viagens_atrasadas = repositorio.buscar_com_atraso()
    print(f"\nViagens com atraso: {len(viagens_atrasadas)}")

    concluidas = repositorio.buscar_por_status("concluida")
    print(f"\nViagens concluídas: {len(concluidas)}")

    print("\nTeste concluído!")

finally:
    repositorio.colecao.database.client.close()
