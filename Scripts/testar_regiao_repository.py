
from Repositories.regiao_repository import RegiaoRepository


repositorio = RegiaoRepository()

try:
    print("=" * 50)
    print("TESTE DO REGIAO REPOSITORY")
    print("=" * 50)

    total = repositorio.contar_documentos()
    print(f"\nTotal de regiões: {total}")

    regiao = repositorio.buscar_por_id("REG0001")
    print("\nConsulta por ID:")
    print(regiao)

    regioes_centro = repositorio.buscar_por_zona("Centro")
    print(f"\nRegiões da zona Centro: {len(regioes_centro)}")

    resultado = repositorio.buscar_por_nome("Setor 001")
    print(f"\nBusca pelo nome 'Setor 001': {len(resultado)}")

finally:
    repositorio.colecao.database.client.close()