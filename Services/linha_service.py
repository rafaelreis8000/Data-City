
from Repositories.linha_repository import LinhaRepository


class LinhaService:

    def __init__(self):
        self.repositorio = LinhaRepository()

    def obter_indicadores_gerais(self) -> dict:

        total = self.repositorio.contar_documentos()

        ativas = self.repositorio.contar_documentos({
            "status": "ativa"
        })

        nao_ativas = total - ativas

        percentual_ativas = (
            (ativas / total) * 100
            if total > 0 else 0
        )

        return {
            "total_linhas": total,
            "linhas_ativas": ativas,
            "linhas_nao_ativas": nao_ativas,
            "percentual_ativas": round(percentual_ativas, 2)
        }

    def obter_distribuicao_por_regiao(self) -> list[dict]:

        pipeline = [
            {
                "$group": {
                    "_id": "$regiao_id",
                    "quantidade": {
                        "$sum": 1
                    }
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
                    "quantidade": {
                        "$sum": 1
                    }
                }
            },
            {
                "$sort": {
                    "quantidade": -1
                }
            }
        ]

        return self.repositorio.executar_agregacao(pipeline)