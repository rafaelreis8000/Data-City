
from Repositories.veiculo_repository import VeiculoRepository


class VeiculoService:

    def __init__(self):
        self.repositorio = VeiculoRepository()

    def obter_indicadores_gerais(self) -> dict:

        total = self.repositorio.contar_documentos()

        ativos = self.repositorio.contar_documentos({
            "status": "ativo"
        })

        inativos = total - ativos

        percentual_ativos = (
            (ativos / total) * 100
            if total > 0 else 0
        )

        return {
            "total_veiculos": total,
            "veiculos_ativos": ativos,
            "veiculos_nao_ativos": inativos,
            "percentual_ativos": round(percentual_ativos, 2)
        }

    def obter_distribuicao_por_combustivel(self) -> list[dict]:

        pipeline = [
            {
                "$group": {
                    "_id": "$tipo_combustivel",
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