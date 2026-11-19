class RelationshipQuality:

    def diagnosticar_relacionamentos(self, dados: dict) -> dict:

        relacionamentos = [
            ("linhas", "regiao_id", "regioes", "_id"),
            ("veiculos", "linha_id", "linhas", "_id"),
            ("viagens", "linha_id", "linhas", "_id"),
            ("viagens", "veiculo_id", "veiculos", "_id"),
            ("viagens", "regiao_id", "regioes", "_id"),
            ("viagens", "ocorrencia_id", "ocorrencias", "_id"),
            ("ocorrencias", "viagem_id", "viagens", "_id"),
            ("ocorrencias", "linha_id", "linhas", "_id")
        ]

        resultados = {}

        for origem, coluna_origem, destino, coluna_destino in relacionamentos:

            referencias = dados[origem][coluna_origem]

            # Valores nulos são ignorados nesta verificação.
            referencias_validas = referencias.dropna()

            ids_destino = dados[destino][coluna_destino]

            # Identifica referências que não existem na coleção de destino.
            referencias_invalidas = referencias_validas[
                ~referencias_validas.isin(ids_destino)
            ]

            chave = f"{origem}.{coluna_origem} -> {destino}.{coluna_destino}"

            resultados[chave] = {
                "total_referencias": len(referencias),
                "referencias_nulas": int(referencias.isna().sum()),
                "referencias_validas": int(
                    len(referencias_validas) - len(referencias_invalidas)
                ),
                "referencias_invalidas": int(
                    len(referencias_invalidas)
                )
            }

        return resultados