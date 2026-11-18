
from Config.database import db

from Repositories.base_repository import BaseRepository


class OcorrenciaRepository(BaseRepository):

    def __init__(self):
        super().__init__(db["ocorrencias"])

    def buscar_por_tipo(self, tipo: str) -> list[dict]:

        return self.buscar_com_filtro({
            "tipo": tipo
        })

    def buscar_por_linha(self, linha_id: str) -> list[dict]:

        return self.buscar_com_filtro({
            "linha_id": linha_id
        })

    def buscar_por_viagem(self, viagem_id: str) -> list[dict]:

        return self.buscar_com_filtro({
            "viagem_id": viagem_id
        })

    def buscar_por_nivel_impacto(
        self,
        nivel: str
    ) -> list[dict]:

        return self.buscar_com_filtro({
            "nivel_impacto": nivel
        })

    def buscar_por_status(self, status: str) -> list[dict]:

        return self.buscar_com_filtro({
            "status": status
        })