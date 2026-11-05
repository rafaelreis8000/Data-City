
from Config.database import client, db, verificar_conexao

try:
    verificar_conexao()

    print("Conexão com MongoDB estabelecida!")
    print(f"Banco de dados: {db.name}")

    colecoes = db.list_collection_names()

    print("\nColeções disponíveis:")

    for colecao in colecoes:
        print(f"- {colecao}")

except Exception as erro:
    print("Erro ao conectar com MongoDB:")
    print(erro)

finally:
    client.close()