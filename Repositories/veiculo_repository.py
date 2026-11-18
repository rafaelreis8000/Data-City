
from Config.database import db

from Repositories.base_repository import BaseRepository


class VeiculoRepository(BaseRepository):

    def __init__(self):
        super().__init__(db["veiculos"])

    def buscar_por_linha(self, linha_id: str) -> list[dict]:

        return self.buscar_com_filtro({
            "linha_id": linha_id
        })

    def buscar_por_status(self, status: str) -> list[dict]:

        return self.buscar_com_filtro({
            "status": status
        })

    def buscar_por_tipo_combustivel(
        self,
        tipo_combustivel: str
    ) -> list[dict]:

        return self.buscar_com_filtro({
            "tipo_combustivel": tipo_combustivel
        })