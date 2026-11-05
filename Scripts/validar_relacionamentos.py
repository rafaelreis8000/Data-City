
from Config.database import db, client


COLECOES = {
    "linhas": db["linhas"],
    "regioes": db["regioes"],
    "veiculos": db["veiculos"],
    "ocorrencias": db["ocorrencias"],
    "viagens": db["viagens"]
}


def validar_referencias(colecao_origem, campo, colecao_destino, campo_destino="_id"):
    referencias = colecao_origem.distinct(campo)

    referencias = [
        referencia for referencia in referencias
        if referencia is not None
    ]

    existentes = set(
        colecao_destino.distinct(campo_destino)
    )

    inexistentes = [
        referencia for referencia in referencias
        if referencia not in existentes
    ]

    return len(referencias), inexistentes


try:
    print("=" * 50)
    print("VALIDAÇÃO DO BANCO DE DADOS - DATA CITY")
    print("=" * 50)

    # 1. Conferir quantidade de documentos

    print("\n1. QUANTIDADE DE DOCUMENTOS")

    for nome, colecao in COLECOES.items():
        total = colecao.count_documents({})
        print(f"{nome}: {total} documentos")

    # 2. Validar relacionamentos das viagens

    print("\n2. VALIDAÇÃO DOS RELACIONAMENTOS")

    relacionamentos = [
        ("linha_id", "linhas"),
        ("veiculo_id", "veiculos"),
        ("regiao_id", "regioes"),
        ("ocorrencia_id", "ocorrencias")
    ]

    for campo, destino in relacionamentos:

        total, inexistentes = validar_referencias(
            COLECOES["viagens"],
            campo,
            COLECOES[destino]
        )

        print(f"\nRelacionamento: viagens -> {destino}")
        print(f"Referências distintas: {total}")
        print(f"Referências inexistentes: {len(inexistentes)}")

        if inexistentes:
            print("Exemplos:", inexistentes[:10])
        else:
            print("Relacionamento validado com sucesso!")

    print("\n" + "=" * 50)
    print("VALIDAÇÃO CONCLUÍDA!")
    print("=" * 50)

except Exception as erro:
    print("\nErro durante a validação:")
    print(erro)

finally:
    client.close()