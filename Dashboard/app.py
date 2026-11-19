
import sys
from pathlib import Path

import streamlit as st
import pandas as pd


# ==========================================================
# 1. CONFIGURACAO DO CAMINHO DO PROJETO
# ==========================================================

RAIZ_PROJETO = Path(__file__).resolve().parent.parent

if str(RAIZ_PROJETO) not in sys.path:
    sys.path.insert(0, str(RAIZ_PROJETO))


# ==========================================================
# 2. IMPORTACAO DOS MODULOS
# ==========================================================

from Analytics.data_loader import DataFrameLoader
from Analytics.data_cleaner import DataCleaner
from Analytics.eda import ExploratoryAnalysis


# ==========================================================
# 3. CONFIGURACAO DA PAGINA
# ==========================================================

st.set_page_config(
    page_title="DataCity Analytics",
    page_icon="🚌",
    layout="wide"
)


# ==========================================================
# 4. FUNCAO PARA FORMATAR VALORES
# ==========================================================

def formatar_valor(valor, casas_decimais=2):

    if pd.isna(valor):
        return 0

    return round(float(valor), casas_decimais)


# ==========================================================
# 5. CARREGAMENTO DOS DADOS
# ==========================================================

@st.cache_data
def carregar_dados():

    loader = DataFrameLoader()

    try:
        dados = loader.carregar_todos()

        limpador = DataCleaner()

        dados_limpos = limpador.limpar_todos(dados)

        return dados_limpos

    finally:
        loader.fechar_conexao()


# ==========================================================
# 6. CABECALHO DO DASHBOARD
# ==========================================================

st.title("🚌 DataCity Analytics")

st.markdown(
    "### Painel de análise do transporte público "
    "de Nova Esperança"
)

st.markdown(
    "Explore indicadores, viagens e ocorrências "
    "do sistema de transporte público."
)

st.divider()


# ==========================================================
# 7. EXECUCAO PRINCIPAL
# ==========================================================

try:

    # ------------------------------------------------------
    # Carregamento das coleções
    # ------------------------------------------------------

    dados = carregar_dados()

    viagens = dados["viagens"]
    ocorrencias = dados["ocorrencias"]
    regioes = dados["regioes"]
    linhas = dados["linhas"]

    analise = ExploratoryAnalysis()


    # ======================================================
    # 8. FILTROS INTERATIVOS
    # ======================================================

    st.sidebar.title("Filtros")

    st.sidebar.markdown(
        "Personalize a consulta utilizando "
        "os filtros abaixo."
    )

    # ------------------------------------------------------
    # Filtro de período
    # ------------------------------------------------------

    data_minima = viagens["data"].min().date()
    data_maxima = viagens["data"].max().date()

    periodo = st.sidebar.date_input(
        "Selecione o período",
        value=(data_minima, data_maxima),
        min_value=data_minima,
        max_value=data_maxima,
        format="DD/MM/YYYY"
    )

    # ------------------------------------------------------
    # Filtro de região
    # ------------------------------------------------------

    regioes_disponiveis = ["Todas"] + sorted(
        regioes["nome"].dropna().unique().tolist()
    )

    regiao_selecionada = st.sidebar.selectbox(
        "Selecione a região",
        regioes_disponiveis
    )

    # ------------------------------------------------------
    # Filtro de linha
    # ------------------------------------------------------

    linhas_disponiveis = ["Todas"] + sorted(
        linhas["codigo"].dropna().unique().tolist()
    )

    linha_selecionada = st.sidebar.selectbox(
        "Selecione a linha",
        linhas_disponiveis
    )


    # ======================================================
    # 9. APLICACAO DOS FILTROS
    # ======================================================

    viagens_filtradas = viagens.copy()

    # ------------------------------------------------------
    # Aplicação do filtro de período
    # ------------------------------------------------------

    if len(periodo) == 2:

        data_inicio, data_fim = periodo

        viagens_filtradas = viagens_filtradas[
            viagens_filtradas["data"].dt.date.between(
                data_inicio,
                data_fim
            )
        ]

    else:

        st.sidebar.warning(
            "Selecione uma data inicial e uma data final."
        )

        viagens_filtradas = viagens_filtradas.iloc[0:0]

    # ------------------------------------------------------
    # Aplicação do filtro de região
    # ------------------------------------------------------

    if regiao_selecionada != "Todas":

        regiao_id = regioes.loc[
            regioes["nome"] == regiao_selecionada,
            "_id"
        ].iloc[0]

        viagens_filtradas = viagens_filtradas[
            viagens_filtradas["regiao_id"] == regiao_id
        ]

    # ------------------------------------------------------
    # Aplicação do filtro de linha
    # ------------------------------------------------------

    if linha_selecionada != "Todas":

        linha_id = linhas.loc[
            linhas["codigo"] == linha_selecionada,
            "_id"
        ].iloc[0]

        viagens_filtradas = viagens_filtradas[
            viagens_filtradas["linha_id"] == linha_id
        ]


    # ======================================================
    # 10. CALCULO DOS INDICADORES
    # ======================================================

    indicadores = analise.analisar_viagens(
        viagens_filtradas
    )


    # ======================================================
    # 11. INDICADORES GERAIS
    # ======================================================

    st.subheader("Indicadores gerais")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total de viagens",
        f"{indicadores['total_viagens']:,}"
    )

    col2.metric(
        "Viagens com atraso",
        f"{indicadores['viagens_com_atraso']:,}"
    )

    col3.metric(
        "Atraso médio",
        f"{formatar_valor(indicadores['atraso_medio_minutos'])} min"
    )

    col4.metric(
        "Avaliação média",
        formatar_valor(indicadores["avaliacao_media"])
    )

    st.divider()


    # ======================================================
    # 12. ANALISE GERAL DAS VIAGENS
    # ======================================================

    st.subheader("Análise das viagens")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Duração média",
            f"{formatar_valor(indicadores['duracao_media_minutos'])} min"
        )

        st.metric(
            "Percentual de viagens atrasadas",
            f"{formatar_valor(indicadores['percentual_atrasos'])}%"
        )

    with col2:

        st.metric(
            "Total de passageiros registrados",
            f"{indicadores['passageiros_total']:,}"
        )

        st.metric(
            "Média de passageiros por viagem",
            formatar_valor(indicadores["passageiros_media"])
        )

    st.divider()


    # ======================================================
    # 13. VIAGENS POR LINHA
    # ======================================================

    st.subheader("Viagens por linha")

    if not viagens_filtradas.empty:

        viagens_por_linha = (
            viagens_filtradas["linha_id"]
            .value_counts()
            .head(10)
            .rename_axis("Linha")
            .reset_index(name="Quantidade de viagens")
        )

        st.bar_chart(
            viagens_por_linha,
            x="Linha",
            y="Quantidade de viagens",
            horizontal=True
        )

    else:

        st.info(
            "Não existem viagens para os filtros selecionados."
        )

    st.divider()


    # ======================================================
    # 14. TABELA DETALHADA DE VIAGENS
    # ======================================================

    st.subheader("Detalhamento das viagens")

    if not viagens_filtradas.empty:

        # Relaciona as viagens com os dados das linhas
        viagens_detalhadas = viagens_filtradas.merge(
            linhas[["_id", "codigo", "nome"]],
            left_on="linha_id",
            right_on="_id",
            how="left",
            suffixes=("", "_linha")
        )

        # Seleciona as colunas que serão exibidas
        colunas_exibidas = [
            "data",
            "hora_saida",
            "hora_chegada",
            "codigo",
            "nome",
            "veiculo_id",
            "duracao_minutos",
            "atraso_minutos",
            "passageiros",
            "avaliacao_media"
        ]

        tabela = viagens_detalhadas[
            colunas_exibidas
        ].copy()

        # Renomeia as colunas
        tabela = tabela.rename(columns={
            "data": "Data",
            "hora_saida": "Saída",
            "hora_chegada": "Chegada",
            "codigo": "Código da linha",
            "nome": "Nome da linha",
            "veiculo_id": "Veículo",
            "duracao_minutos": "Duração (min)",
            "atraso_minutos": "Atraso (min)",
            "passageiros": "Passageiros",
            "avaliacao_media": "Avaliação"
        })

        # Formata a data
        tabela["Data"] = tabela["Data"].dt.strftime(
            "%d/%m/%Y"
        )

        # Controle da quantidade de registros exibidos
        quantidade_exibida = st.number_input(
            "Quantidade de viagens para exibir",
            min_value=10,
            max_value=1000,
            value=100,
            step=10
        )

        st.dataframe(
            tabela.head(quantidade_exibida),
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            f"Total de viagens encontradas: "
            f"{len(tabela):,} | "
            f"Registros exibidos: "
            f"{min(len(tabela), quantidade_exibida):,}"
        )

    else:

        st.info(
            "Não existem viagens para os filtros selecionados."
        )

    st.divider()


    # ======================================================
    # 15. ANALISE DAS OCORRENCIAS
    # ======================================================

    st.subheader("Análise das ocorrências")

    # Identifica as viagens que passaram pelos filtros
    ids_viagens_filtradas = set(
        viagens_filtradas["_id"]
    )

    # Busca ocorrências relacionadas às viagens filtradas
    ocorrencias_filtradas = ocorrencias[
        ocorrencias["viagem_id"].isin(
            ids_viagens_filtradas
        )
    ]

    col1, col2 = st.columns(2)

    # ------------------------------------------------------
    # Ocorrências por tipo
    # ------------------------------------------------------

    with col1:

        st.markdown("**Ocorrências por tipo**")

        if not ocorrencias_filtradas.empty:

            ocorrencias_tipo = (
                ocorrencias_filtradas["tipo"]
                .value_counts()
                .rename_axis("Tipo")
                .reset_index(name="Quantidade")
            )

            st.bar_chart(
                ocorrencias_tipo,
                x="Tipo",
                y="Quantidade"
            )

        else:

            st.info(
                "Nenhuma ocorrência encontrada "
                "para os filtros selecionados."
            )

    # ------------------------------------------------------
    # Ocorrências por nível de impacto
    # ------------------------------------------------------

    with col2:

        st.markdown("**Ocorrências por nível de impacto**")

        if not ocorrencias_filtradas.empty:

            ocorrencias_impacto = (
                ocorrencias_filtradas["nivel_impacto"]
                .value_counts()
                .rename_axis("Impacto")
                .reset_index(name="Quantidade")
            )

            st.bar_chart(
                ocorrencias_impacto,
                x="Impacto",
                y="Quantidade"
            )

        else:

            st.info(
                "Nenhuma ocorrência encontrada "
                "para os filtros selecionados."
            )

    st.divider()


    # ======================================================
    # 16. RESUMO DA CONSULTA
    # ======================================================

    st.subheader("Resumo da consulta")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Viagens selecionadas",
        f"{len(viagens_filtradas):,}"
    )

    col2.metric(
        "Ocorrências relacionadas",
        f"{len(ocorrencias_filtradas):,}"
    )

    col3.metric(
        "Região selecionada",
        regiao_selecionada
    )

    col4.metric(
        "Linha selecionada",
        linha_selecionada
    )


    # ======================================================
    # 17. RODAPE
    # ======================================================

    st.divider()

    st.caption(
        "DataCity Analytics | Projeto acadêmico | "
        "Dados sintéticos para fins de análise."
    )


# ==========================================================
# 18. TRATAMENTO DE ERROS
# ==========================================================

except Exception as erro:

    st.error(
        f"Não foi possível carregar o Dashboard: {erro}"
    )

    st.exception(erro)