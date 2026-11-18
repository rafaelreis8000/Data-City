
from Config.database import db

from Repositories.base_repository import BaseRepository


class ViagemRepository(BaseRepository):

    def __init__(self):
        super().__init__(db["viagens"])

    def buscar_por_linha(self, linha_id: str) -> list[dict]:

        return self.buscar_com_filtro({
            "linha_id": linha_id
        })

    def buscar_por_veiculo(self, veiculo_id: str) -> list[dict]:

        return self.buscar_com_filtro({
            "veiculo_id": veiculo_id
        })

    def buscar_com_atraso(self) -> list[dict]:

        return self.buscar_com_filtro({
            "atraso_minutos": {
                "$gt": 0
            }
        })

    def buscar_por_status(self, status: str) -> list[dict]:

        return self.buscar_com_filtro({
            "status": status
        })