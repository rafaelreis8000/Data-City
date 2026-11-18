
from Config.database import db

from Repositories.base_repository import BaseRepository


class LinhaRepository(BaseRepository):

    def __init__(self):
        super().__init__(db["linhas"])

    def buscar_por_regiao(self, regiao_id: str) -> list[dict]:

        return self.buscar_com_filtro({
            "regiao_id": regiao_id
        })

    def buscar_ativas(self) -> list[dict]:

        return self.buscar_com_filtro({
            "status": "ativa"
        })
