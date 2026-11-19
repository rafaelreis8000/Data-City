# Construção visual dos dados
import matplotlib.pyplot as plt
from pathlib import Path


class DataVisualization:

    def __init__(self):
        self.pasta_graficos = Path("outputs/graficos")
        self.pasta_graficos.mkdir(
            parents=True,
            exist_ok=True
        )

    def gerar_viagens_por_linha(
        self,
        dataframe
    ):

        dados = (
            dataframe["linha_id"]
            .value_counts()
            .head(10)
            .sort_values()
        )

        plt.figure(figsize=(10, 6))

        dados.plot(kind="barh")

        plt.title("Top 10 linhas por quantidade de viagens")
        plt.xlabel("Quantidade de viagens")
        plt.ylabel("Linha")

        plt.tight_layout()

        plt.savefig(
            self.pasta_graficos / "viagens_por_linha.png",
            dpi=300
        )

        plt.close()

    def gerar_ocorrencias_por_tipo(
        self,
        dataframe
    ):

        dados = dataframe["tipo"].value_counts()

        plt.figure(figsize=(10, 6))

        dados.plot(kind="bar")

        plt.title("Ocorrências por tipo")
        plt.xlabel("Tipo de ocorrência")
        plt.ylabel("Quantidade")

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.savefig(
            self.pasta_graficos / "ocorrencias_por_tipo.png",
            dpi=300
        )

        plt.close()

    def gerar_ocorrencias_por_impacto(
        self,
        dataframe
    ):

        dados = dataframe["nivel_impacto"].value_counts()

        plt.figure(figsize=(8, 6))

        dados.plot(kind="bar")

        plt.title("Ocorrências por nível de impacto")
        plt.xlabel("Nível de impacto")
        plt.ylabel("Quantidade")

        plt.xticks(rotation=0)

        plt.tight_layout()

        plt.savefig(
            self.pasta_graficos / "ocorrencias_por_impacto.png",
            dpi=300
        )

        plt.close()

    def gerar_todos(self, dados):

        self.gerar_viagens_por_linha(
            dados["viagens"]
        )

        self.gerar_ocorrencias_por_tipo(
            dados["ocorrencias"]
        )

        self.gerar_ocorrencias_por_impacto(
            dados["ocorrencias"]
        )