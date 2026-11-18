
from Repositories.ocorrencia_repository import OcorrenciaRepository


repositorio = OcorrenciaRepository()

try:
    print("=" * 50)
    print("TESTE DO OCORRENCIA REPOSITORY")
    print("=" * 50)

    total = repositorio.contar_documentos()
    print(f"\nTotal de ocorrências: {total}")

    ocorrencia = repositorio.buscar_por_id("OCO000001")
    print("\nConsulta por ID:")
    print(ocorrencia)

    acidentes = repositorio.buscar_por_tipo("Acidente")
    print(f"\nOcorrências do tipo Acidente: {len(acidentes)}")

    ocorrencias_linha = repositorio.buscar_por_linha("LIN0143")
    print(f"\nOcorrências da linha LIN0143: {len(ocorrencias_linha)}")

    impacto_baixo = repositorio.buscar_por_nivel_impacto("Baixo")
    print(f"\nOcorrências de baixo impacto: {len(impacto_baixo)}")

    print("\nTeste concluído!")

finally:
    repositorio.colecao.database.client.close()