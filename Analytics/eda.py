#Calcula indicadores, compara desempenho das linhas e investiga os impactos e ocorrências
import pandas as pd


class ExploratoryAnalysis:

    def analisar_viagens(
        self,
        dataframe: pd.DataFrame
    ) -> dict:

        total_viagens = len(dataframe)

        viagens_com_atraso = dataframe[
            dataframe["atraso_minutos"] > 0
        ]

        percentual_atrasos = (
            len(viagens_com_atraso) / total_viagens * 100
            if total_viagens > 0
            else 0
        )

        resultado = {
            "total_viagens": total_viagens,

            "viagens_com_atraso": len(viagens_com_atraso),

            "percentual_atrasos": round(
                percentual_atrasos, 2
            ),

            "atraso_medio_minutos": round(
                viagens_com_atraso["atraso_minutos"].mean(),
                2
            ) if not viagens_com_atraso.empty else 0,

            "duracao_media_minutos": round(
                dataframe["duracao_minutos"].mean(), 2
            ),

            "passageiros_total": int(
                dataframe["passageiros"].sum()
            ),

            "passageiros_media": round(
                dataframe["passageiros"].mean(), 2
            ),

            "avaliacao_media": round(
                dataframe["avaliacao_media"].mean(), 2
            )
        }

        return resultado

    def analisar_viagens_por_linha(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        resultado = (
            dataframe.groupby("linha_id")
            .agg(
                total_viagens=("_id", "count"),
                atraso_medio=("atraso_minutos", "mean"),
                passageiros_total=("passageiros", "sum"),
                avaliacao_media=("avaliacao_media", "mean")
            )
            .reset_index()
        )

        resultado["atraso_medio"] = (
            resultado["atraso_medio"].round(2)
        )

        resultado["avaliacao_media"] = (
            resultado["avaliacao_media"].round(2)
        )

        return resultado.sort_values(
            by="total_viagens",
            ascending=False
        )

    def analisar_ocorrencias(
        self,
        dataframe: pd.DataFrame
    ) -> dict:

        return {
            "total_ocorrencias": len(dataframe),

            "ocorrencias_por_tipo": (
                dataframe["tipo"].value_counts()
            ),

            "ocorrencias_por_impacto": (
                dataframe["nivel_impacto"].value_counts()
            ),

            "ocorrencias_por_status": (
                dataframe["status"].value_counts()
            )
        }