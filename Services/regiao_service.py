
from Repositories.regiao_repository import RegiaoRepository


class RegiaoService:

    def __init__(self):
        self.repositorio = RegiaoRepository()

    def obter_indicadores_gerais(self) -> dict:

        pipeline = [
            {
                "$group": {
                    "_id": None,
                    "total_regioes": {"$sum": 1},
                    "populacao_total_estimada": {
                        "$sum": "$populacao_estimada"
                    },
                    "area_total_km2": {
                        "$sum": "$area_km2"
                    }
                }
            }
        ]

        resultado = self.repositorio.executar_agregacao(pipeline)

        if not resultado:
            return {
                "total_regioes": 0,
                "populacao_total_estimada": 0,
                "area_total_km2": 0
            }

        indicadores = resultado[0]

        return {
            "total_regioes": indicadores["total_regioes"],
            "populacao_total_estimada": indicadores[
                "populacao_total_estimada"
            ],
            "area_total_km2": round(
                indicadores["area_total_km2"], 2
            )
        }

    def obter_distribuicao_por_zona(self) -> list[dict]:

        pipeline = [
            {
                "$group": {
                    "_id": "$zona",
                    "quantidade_regioes": {"$sum": 1},
                    "populacao_estimada": {
                        "$sum": "$populacao_estimada"
                    },
                    "area_total_km2": {
                        "$sum": "$area_km2"
                    }
                }
            },
            {
                "$sort": {
                    "quantidade_regioes": -1
                }
            }
        ]

        return self.repositorio.executar_agregacao(pipeline)

    def buscar_regioes_por_zona(self, zona: str) -> list[dict]:

        return self.repositorio.buscar_por_zona(zona)