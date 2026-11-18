#busca os documentos do MongoDB e transforma em DataFrames do Pandas
import pandas as pd

from Repositories.linha_repository import LinhaRepository
from Repositories.regiao_repository import RegiaoRepository
from Repositories.veiculo_repository import VeiculoRepository
from Repositories.viagem_repository import ViagemRepository
from Repositories.ocorrencia_repository import OcorrenciaRepository


class DataFrameLoader:

    def __init__(self):
        self.repositorios = {
            "linhas": LinhaRepository(),
            "regioes": RegiaoRepository(),
            "veiculos": VeiculoRepository(),
            "viagens": ViagemRepository(),
            "ocorrencias": OcorrenciaRepository()
        }

    def carregar_colecao(self, nome: str) -> pd.DataFrame:

        if nome not in self.repositorios:
            raise ValueError(
                f"Coleção não encontrada: {nome}"
            )

        documentos = self.repositorios[nome].buscar_todos()

        return pd.DataFrame(documentos)

    def carregar_todos(self) -> dict[str, pd.DataFrame]:

        dados = {}

        for nome in self.repositorios:
            dados[nome] = self.carregar_colecao(nome)

        return dados

    def fechar_conexao(self):

        repositorio = self.repositorios["viagens"]

        repositorio.colecao.database.client.close()
