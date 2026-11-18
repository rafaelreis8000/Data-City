
from typing import Any

from pymongo.collection import Collection


class BaseRepository:
    """
    Classe responsável pelas operações básicas
    de consulta às coleções do MongoDB.
    """

    def __init__(self, colecao: Collection):
        self.colecao = colecao

    def buscar_todos(
        self,
        filtro: dict | None = None,
        limite: int = 0
    ) -> list[dict]:

        filtro = filtro or {}

        cursor = self.colecao.find(filtro)

        if limite > 0:
            cursor = cursor.limit(limite)

        return list(cursor)

    def buscar_por_id(self, documento_id: str) -> dict | None:

        return self.colecao.find_one({"_id": documento_id})

    def buscar_com_filtro(
        self,
        filtro: dict,
        limite: int = 0
    ) -> list[dict]:

        cursor = self.colecao.find(filtro)

        if limite > 0:
            cursor = cursor.limit(limite)

        return list(cursor)

    def contar_documentos(
        self,
        filtro: dict | None = None
    ) -> int:

        filtro = filtro or {}

        return self.colecao.count_documents(filtro)
    
    def executar_agregacao(self, pipeline: list [dict]) -> list [dict]:
        return list(self.colecao.aggregate(pipeline))