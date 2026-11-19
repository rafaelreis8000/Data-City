
import pandas as pd


class DataQuality:

    def diagnosticar_dataframe(self, dataframe: pd.DataFrame) -> dict:

        total_registros = len(dataframe)

        valores_ausentes = dataframe.isnull().sum()

        percentual_ausentes = (
            (valores_ausentes / total_registros) * 100
            if total_registros > 0
            else valores_ausentes
        )

        # Diagnóstico de valores únicos
        valores_unicos = {}

        for coluna in dataframe.columns:

            valores = dataframe[coluna].apply(
                lambda valor: str(valor)
                if isinstance(valor, (dict, list))
                else valor
            )

            valores_unicos[coluna] = valores.nunique(
                dropna=True
            )

        # Cria uma cópia normalizada para verificar
        # duplicidades sem modificar o DataFrame original.
        dataframe_comparacao = dataframe.copy()

        for coluna in dataframe_comparacao.columns:

            dataframe_comparacao[coluna] = (
                dataframe_comparacao[coluna].apply(
                    lambda valor: str(valor)
                    if isinstance(valor, (dict, list))
                    else valor
                )
            )

        registros_duplicados = int(
            dataframe_comparacao.duplicated().sum()
        )

        # Verifica identificadores duplicados
        ids_duplicados = 0

        if "_id" in dataframe.columns:

            ids_duplicados = int(
                dataframe["_id"].duplicated().sum()
            )

        diagnostico_colunas = pd.DataFrame({
            "tipo_dado": dataframe.dtypes.astype(str),
            "valores_ausentes": valores_ausentes,
            "percentual_ausentes": percentual_ausentes.round(2),
            "valores_unicos": pd.Series(valores_unicos)
        })

        return {
            "total_registros": total_registros,
            "total_colunas": len(dataframe.columns),
            "registros_duplicados": registros_duplicados,
            "ids_duplicados": ids_duplicados,
            "diagnostico_colunas": diagnostico_colunas
        }

    def diagnosticar_todos(
        self,
        dados: dict[str, pd.DataFrame]
    ) -> dict:

        resultados = {}

        for nome, dataframe in dados.items():

            resultados[nome] = self.diagnosticar_dataframe(
                dataframe
            )

        return resultados