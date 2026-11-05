
from pathlib import Path
from bson import json_util

from Config.database import db, client


DATA_DIR = Path(__file__).resolve().parents[1] / "data"

ARQUIVO = DATA_DIR / "ocorrencias.json"
COLECAO = db["ocorrencias"]

try:
    if not ARQUIVO.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {ARQUIVO}")

    if COLECAO.count_documents({}) > 0:
        raise RuntimeError(
            "A coleção ocorrencias já possui documentos. "
            "Importação interrompida para evitar duplicações."
        )

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        documentos = json_util.loads(arquivo.read())

    if not isinstance(documentos, list):
        raise ValueError("O arquivo JSON não contém uma lista.")

    tamanho_lote = 1000

    for inicio in range(0, len(documentos), tamanho_lote):
        lote = documentos[inicio:inicio + tamanho_lote]
        COLECAO.insert_many(lote)

        print(
            f"Importados: {min(inicio + tamanho_lote, len(documentos))}"
        )

    total = COLECAO.count_documents({})

    print("\nImportação concluída com sucesso!")
    print(f"Documentos no arquivo: {len(documentos)}")
    print(f"Documentos na coleção: {total}")

except Exception as erro:
    print("Erro durante a importação:")
    print(erro)

finally:
    client.close()