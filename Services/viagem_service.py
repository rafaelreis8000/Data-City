
from Repositories.viagem_repository import ViagemRepository


class ViagemService:

    def __init__(self):
        self.repositorio = ViagemRepository()

    def obter_indicadores_gerais(self) -> dict:

        pipeline = [
            {
                "$group": {
                    "_id": None,

                    "total_viagens": {
                        "$sum": 1
                    },

                    "viagens_com_atraso": {
                        "$sum": {
                            "$cond": [
                                {"$gt": ["$atraso_minutos", 0]},
                                1,
                                0
                            ]
                        }
                    },

                    "media_atraso_minutos": {
                        "$avg": {
                            "$cond": [
                                {"$gt": ["$atraso_minutos", 0]},
                                "$atraso_minutos",
                                None
                            ]
                        }
                    },

                    "total_passageiros": {
                        "$sum": "$passageiros"
                    },

                    "duracao_media_minutos": {
                        "$avg": "$duracao_minutos"
                    }
                }
            }
        ]

        resultado = self.repositorio.executar_agregacao(pipeline)

        if not resultado:
            return {
                "total_viagens": 0,
                "viagens_com_atraso": 0,
                "percentual_atrasos": 0,
                "media_atraso_minutos": 0,
                "total_passageiros": 0,
                "duracao_media_minutos": 0
            }

        indicadores = resultado[0]

        total = indicadores["total_viagens"]
        atrasadas = indicadores["viagens_com_atraso"]

        percentual = (
            (atrasadas / total) * 100
            if total > 0 else 0
        )

        return {
            "total_viagens": total,
            "viagens_com_atraso": atrasadas,
            "percentual_atrasos": round(percentual, 2),
            "media_atraso_minutos": round(
                indicadores["media_atraso_minutos"] or 0, 2
            ),
            "total_passageiros": indicadores["total_passageiros"],
            "duracao_media_minutos": round(
                indicadores["duracao_media_minutos"] or 0, 2
            )
        }