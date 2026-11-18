
from Repositories.linha_repository import LinhaRepository


repositorio = LinhaRepository()

try:
    print("=" * 50)
    print("TESTE DO LINHA REPOSITORY")
    print("=" * 50)

    total = repositorio.contar_documentos()

    print(f"\nTotal de linhas: {total}")

    linha = repositorio.buscar_por_id("LIN0001")

    print("\nConsulta por ID:")
    print(linha)

    linhas_ativas = repositorio.buscar_ativas()

    print(f"\nLinhas ativas: {len(linhas_ativas)}")

    print("\nTeste concluído!")

finally:
    repositorio.colecao.database.client.close()