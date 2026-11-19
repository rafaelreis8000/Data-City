#Utilizado para preparar os dataframes
import pandas as pd


class DataCleaner:

    def limpar_dataframe(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        # Cria uma cópia para preservar os dados originais.
        dataframe_limpo = dataframe.copy()

        # Remove espaços desnecessários no início e no final
        # dos valores textuais.
        for coluna in dataframe_limpo.columns:

            dataframe_limpo[coluna] = (
                dataframe_limpo[coluna].map(
                    lambda valor: valor.strip()
                    if isinstance(valor, str)
                    else valor
                )
            )

        return dataframe_limpo

    def limpar_todos(
        self,
        dados: dict[str, pd.DataFrame]
    ) -> dict[str, pd.DataFrame]:

        dados_limpos = {}

        for nome, dataframe in dados.items():

            dados_limpos[nome] = self.limpar_dataframe(
                dataframe
            )

        return dados_limpos