
from Repositories.ocorrencia_repository import OcorrenciaRepository


class OcorrenciaService:

    def __init__(self):
        self.repositorio = OcorrenciaRepository()

    def obter_indicadores_gerais(self) -> dict:

        total = self.repositorio.contar_documentos()

        pipeline = [
            {
                "$group": {
                    "_id": None,
                    "total_ocorrencias": {"$sum": 1},
                    "baixo_impacto": {
                        "$sum": {
                            "$cond": [
                                {"$eq": ["$nivel_impacto", "Baixo"]},
                                1,
                                0
                            ]
                        }
                    },
                    "medio_impacto": {
                        "$sum": {
                            "$cond": [
                                {"$eq": ["$nivel_impacto", "Médio"]},
                                1,
                                0
                            ]
                        }
                    },
                    "alto_impacto": {
                        "$sum": {
                            "$cond": [
                                {"$eq": ["$nivel_impacto", "Alto"]},
                                1,
                                0
                            ]
                        }
                    }
                }
            }
        ]

        resultado = self.repositorio.executar_agregacao(pipeline)

        if not resultado:
            return {
                "total_ocorrencias": total,
                "baixo_impacto": 0,
                "medio_impacto": 0,
                "alto_impacto": 0
            }

        indicadores = resultado[0]

        return {
            "total_ocorrencias": indicadores["total_ocorrencias"],
            "baixo_impacto": indicadores["baixo_impacto"],
            "medio_impacto": indicadores["medio_impacto"],
            "alto_impacto": indicadores["alto_impacto"]
        }

    def obter_distribuicao_por_tipo(self) -> list[dict]:

        pipeline = [
            {
                "$group": {
                    "_id": "$tipo",
                    "quantidade": {"$sum": 1}
                }
            },
            {
                "$sort": {
                    "quantidade": -1
                }
            }
        ]

        return self.repositorio.executar_agregacao(pipeline)

    def obter_distribuicao_por_impacto(self) -> list[dict]:

        pipeline = [
            {
                "$group": {
                    "_id": "$nivel_impacto",
                    "quantidade": {"$sum": 1}
                }
            },
            {
                "$sort": {
                    "quantidade": -1
                }
            }
        ]

        return self.repositorio.executar_agregacao(pipeline)

    def obter_distribuicao_por_status(self) -> list[dict]:

        pipeline = [
            {
                "$group": {
                    "_id": "$status",
                    "quantidade": {"$sum": 1}
                }
            },
            {
                "$sort": {
                    "quantidade": -1
                }
            }
        ]

        return self.repositorio.executar_agregacao(pipeline)