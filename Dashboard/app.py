#Configuração da Dashboard
import sys
from pathlib import Path

# ==========================================================
# 1. CONFIGURACAO DO CAMINHO DO PROJETO
# ==========================================================

RAIZ_PROJETO = Path(__file__).resolve().parent.parent

if str(RAIZ_PROJETO) not in sys.path:
    sys.path.insert(0, str(RAIZ_PROJETO))


# ==========================================================
# 2. IMPORTACAO DAS BIBLIOTECAS E MODULOS
# ==========================================================

import streamlit as st
import pandas as pd

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
# 4. CARREGAMENTO E PREPARACAO DOS DADOS
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
# 5. CABECALHO DO DASHBOARD
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
# 6. EXECUCAO PRINCIPAL DO DASHBOARD
# ==========================================================

try:

    # Carrega os dados
    dados = carregar_dados()

    # Inicializa a classe de análise
    analise = ExploratoryAnalysis()

    # Seleciona os DataFrames
    viagens = dados["viagens"]
    ocorrencias = dados["ocorrencias"]

    # Calcula os indicadores
    indicadores = analise.analisar_viagens(viagens)


    # ======================================================
    # 7. INDICADORES GERAIS
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
        f"{indicadores['atraso_medio_minutos']} min"
    )

    col4.metric(
        "Avaliação média",
        indicadores["avaliacao_media"]
    )

    st.divider()


    # ======================================================
    # 8. ANALISE GERAL DAS VIAGENS
    # ======================================================

    st.subheader("Análise das viagens")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Duração média",
            f"{indicadores['duracao_media_minutos']} min"
        )

        st.metric(
            "Percentual de viagens atrasadas",
            f"{indicadores['percentual_atrasos']}%"
        )

    with col2:

        st.metric(
            "Total de passageiros registrados",
            f"{indicadores['passageiros_total']:,}"
        )

        st.metric(
            "Média de passageiros por viagem",
            indicadores["passageiros_media"]
        )

    st.divider()


    # ======================================================
    # 9. VIAGENS POR LINHA
    # ======================================================

    st.subheader("Viagens por linha")

    viagens_por_linha = (
        viagens["linha_id"]
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

    st.divider()


    # ======================================================
    # 10. ANALISE DAS OCORRENCIAS
    # ======================================================

    st.subheader("Análise das ocorrências")

    col1, col2 = st.columns(2)

    # Ocorrências por tipo
    with col1:

        st.markdown("**Ocorrências por tipo**")

        ocorrencias_tipo = (
            ocorrencias["tipo"]
            .value_counts()
            .rename_axis("Tipo")
            .reset_index(name="Quantidade")
        )

        st.bar_chart(
            ocorrencias_tipo,
            x="Tipo",
            y="Quantidade"
        )

    # Ocorrências por impacto
    with col2:

        st.markdown("**Ocorrências por nível de impacto**")

        ocorrencias_impacto = (
            ocorrencias["nivel_impacto"]
            .value_counts()
            .rename_axis("Impacto")
            .reset_index(name="Quantidade")
        )

        st.bar_chart(
            ocorrencias_impacto,
            x="Impacto",
            y="Quantidade"
        )

    st.divider()


    # ======================================================
    # 11. RODAPE
    # ======================================================

    st.caption(
        "DataCity Analytics | "
        "Projeto acadêmico | "
        "Dados sintéticos para fins de análise."
    )


# ==========================================================
# 12. TRATAMENTO DE ERROS
# ==========================================================

except Exception as erro:

    st.error(
        f"Não foi possível carregar o Dashboard: {erro}"
    )

    st.exception(erro)