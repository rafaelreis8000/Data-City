
from Config.database import db

from Repositories.base_repository import BaseRepository


class RegiaoRepository(BaseRepository):

    def __init__(self):
        super().__init__(db["regioes"])

    def buscar_por_zona(self, zona: str) -> list[dict]:

        return self.buscar_com_filtro({
            "zona": zona
        })

    def buscar_por_nome(self, nome: str) -> list[dict]:

        return self.buscar_com_filtro({
            "nome": {
                "$regex": nome,
                "$options": "i"
            }
        })