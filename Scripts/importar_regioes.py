
from pathlib import Path
from bson import json_util

from Config.database import db, client


# Caminho da pasta que contém os arquivos JSON
DATA_DIR = Path(__file__).resolve().parents[1] / "data"

# Arquivo e coleção que serão importados
ARQUIVO = DATA_DIR / "regioes.json"
COLECAO = db["regioes"]

try:
    # Verifica se o arquivo existe
    if not ARQUIVO.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {ARQUIVO}"
        )

    # Evita inserir os mesmos documentos novamente
    if COLECAO.count_documents({}) > 0:
        raise RuntimeError(
            "A coleção regioes já possui documentos. "
            "A importação foi interrompida."
        )

    # Lê os dados preservando os tipos BSON do Extended JSON
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        documentos = json_util.loads(arquivo.read())

    if not isinstance(documentos, list):
        raise ValueError("O arquivo JSON não contém uma lista.")

    # Importa os documentos em lotes
    tamanho_lote = 1000

    for inicio in range(0, len(documentos), tamanho_lote):
        lote = documentos[inicio:inicio + tamanho_lote]
        COLECAO.insert_many(lote)

    # Confirma a quantidade importada
    total = COLECAO.count_documents({})

    print("Importação concluída com sucesso!")
    print(f"Documentos no arquivo: {len(documentos)}")
    print(f"Documentos na coleção: {total}")

except Exception as erro:
    print("Erro durante a importação:")
    print(erro)

finally:
    client.close()