
import pandas as pd


class DataIntegrity:

    def verificar_relacionamento(
        self,
        dataframe_origem: pd.DataFrame,
        coluna_origem: str,
        dataframe_destino: pd.DataFrame,
        coluna_destino: str = "_id"
    ) -> dict:

        referencias = dataframe_origem[coluna_origem]

        referencias_validas = referencias.dropna()

        valores_destino = dataframe_destino[coluna_destino]

        referencias_invalidas = referencias_validas[
            ~referencias_validas.isin(valores_destino)
        ]

        return {
            "total_referencias": len(referencias),
            "referencias_nulas": int(referencias.isna().sum()),
            "referencias_invalidas": len(referencias_invalidas),
            "exemplos_invalidos": (
                referencias_invalidas.unique()[:5].tolist()
            )
        }

    def verificar_todos(self, dados: dict) -> dict:

        relacionamentos = [
            ("linhas", "regiao_id", "regioes"),
            ("veiculos", "linha_id", "linhas"),
            ("viagens", "linha_id", "linhas"),
            ("viagens", "veiculo_id", "veiculos"),
            ("viagens", "regiao_id", "regioes"),
            ("viagens", "ocorrencia_id", "ocorrencias"),
            ("ocorrencias", "viagem_id", "viagens"),
            ("ocorrencias", "linha_id", "linhas")
        ]

        resultados = {}

        for origem, coluna, destino in relacionamentos:

            nome = f"{origem}.{coluna} -> {destino}._id"

            resultados[nome] = self.verificar_relacionamento(
                dataframe_origem=dados[origem],
                coluna_origem=coluna,
                dataframe_destino=dados[destino]
            )

        return resultados