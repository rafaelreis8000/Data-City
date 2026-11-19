
import sys
import json
from pathlib import Path

import streamlit as st
import pandas as pd
import folium

from folium.plugins import FastMarkerCluster
from streamlit_folium import st_folium


# ============================================================
# 1. CONFIGURAÇÃO DOS CAMINHOS
# ============================================================

RAIZ_PROJETO = Path(__file__).resolve().parents[2]

if str(RAIZ_PROJETO) not in sys.path:
    sys.path.insert(0, str(RAIZ_PROJETO))


# ============================================================
# 2. IMPORTAÇÕES DO PROJETO
# ============================================================

from Analytics.data_loader import DataFrameLoader
from Analytics.data_cleaner import DataCleaner


# ============================================================
# 3. CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Nova Esperança | Mapa Geográfico",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ Nova Esperança — Distribuição Geográfica")

st.markdown(
    """
    Esta página apresenta a distribuição espacial das regiões
    atendidas pelo sistema de transporte público fictício de
    **Nova Esperança**, além das ocorrências registradas nas viagens.

    Os dados geográficos são sintéticos e representam a organização
    territorial simulada da cidade.
    """
)


# ============================================================
# 4. CARREGAMENTO DOS DADOS
# ============================================================

@st.cache_data
def carregar_dados():

    loader = DataFrameLoader()

    dados = loader.carregar_todos()

    cleaner = DataCleaner()

    dados_limpos = {}

    for nome, dataframe in dados.items():

        dados_limpos[nome] = cleaner.limpar_dataframe(
            dataframe
        )

    return dados_limpos


try:

    dados = carregar_dados()

    regioes = dados["regioes"].copy()
    ocorrencias = dados["ocorrencias"].copy()

except Exception as erro:

    st.error(f"Erro ao carregar os dados: {erro}")
    st.stop()


# ============================================================
# 5. EXTRAÇÃO DAS COORDENADAS GEOJSON
# ============================================================

def extrair_coordenadas(localizacao):
    """
    Recebe uma localização GeoJSON e retorna:
    (latitude, longitude).

    Aceita dicionários e strings JSON.
    """

    if isinstance(localizacao, str):

        try:

            localizacao = json.loads(localizacao)

        except (json.JSONDecodeError, TypeError):

            return None

    if not isinstance(localizacao, dict):

        return None

    coordenadas = localizacao.get("coordinates")

    if not isinstance(coordenadas, (list, tuple)):

        return None

    if len(coordenadas) < 2:

        return None

    try:

        longitude = float(coordenadas[0])
        latitude = float(coordenadas[1])

    except (ValueError, TypeError):

        return None

    if not (-90 <= latitude <= 90):

        return None

    if not (-180 <= longitude <= 180):

        return None

    return latitude, longitude


# ============================================================
# 6. PREPARAÇÃO DOS DADOS GEOGRÁFICOS
# ============================================================

if "geom" not in regioes.columns:

    st.error(
        "A coluna 'geom' não foi encontrada na coleção de regiões."
    )

    st.stop()


if "localizacao" not in ocorrencias.columns:

    st.error(
        "A coluna 'localizacao' não foi encontrada "
        "na coleção de ocorrências."
    )

    st.stop()


# Coordenadas das regiões

regioes["coordenadas"] = regioes["geom"].apply(
    extrair_coordenadas
)

regioes_mapa = regioes[
    regioes["coordenadas"].notna()
].copy()


if not regioes_mapa.empty:

    regioes_mapa[
        ["latitude", "longitude"]
    ] = pd.DataFrame(
        regioes_mapa["coordenadas"].tolist(),
        index=regioes_mapa.index
    )


# Coordenadas das ocorrências

ocorrencias["coordenadas"] = ocorrencias["localizacao"].apply(
    extrair_coordenadas
)

ocorrencias_mapa = ocorrencias[
    ocorrencias["coordenadas"].notna()
].copy()


if not ocorrencias_mapa.empty:

    ocorrencias_mapa[
        ["latitude", "longitude"]
    ] = pd.DataFrame(
        ocorrencias_mapa["coordenadas"].tolist(),
        index=ocorrencias_mapa.index
    )


# ============================================================
# 7. DIAGNÓSTICO DOS DADOS
# ============================================================

with st.expander("Diagnóstico dos dados geográficos"):

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Total de regiões",
            len(regioes)
        )

        st.metric(
            "Regiões com coordenadas válidas",
            len(regioes_mapa)
        )

    with col2:

        st.metric(
            "Total de ocorrências",
            len(ocorrencias)
        )

        st.metric(
            "Ocorrências com coordenadas válidas",
            len(ocorrencias_mapa)
        )

    st.write("Exemplo de geometria de uma região:")

    if not regioes.empty:

        st.write(regioes["geom"].iloc[0])

    st.write("Exemplo de localização de uma ocorrência:")

    if not ocorrencias.empty:

        st.write(ocorrencias["localizacao"].iloc[0])


# ============================================================
# 8. FILTROS
# ============================================================

st.subheader("Filtros geográficos")

col1, col2, col3 = st.columns(3)


# Filtro de regiões

with col1:

    if "nome" in regioes_mapa.columns:

        regioes_disponiveis = sorted(
            regioes_mapa["nome"].dropna().unique().tolist()
        )

        regioes_selecionadas = st.multiselect(
            "Regiões",
            options=regioes_disponiveis,
            default=regioes_disponiveis
        )

    else:

        regioes_selecionadas = []


# Filtro de tipos de ocorrência

with col2:

    if "tipo" in ocorrencias_mapa.columns:

        tipos_disponiveis = sorted(
            ocorrencias_mapa["tipo"].dropna().unique().tolist()
        )

        tipos_selecionados = st.multiselect(
            "Tipos de ocorrência",
            options=tipos_disponiveis,
            default=tipos_disponiveis
        )

    else:

        tipos_selecionados = []


# Filtro de nível de impacto

with col3:

    if "nivel_impacto" in ocorrencias_mapa.columns:

        impactos_disponiveis = sorted(
            ocorrencias_mapa["nivel_impacto"].dropna().unique().tolist()
        )

        impactos_selecionados = st.multiselect(
            "Nível de impacto",
            options=impactos_disponiveis,
            default=impactos_disponiveis
        )

    else:

        impactos_selecionados = []


# ============================================================
# 9. APLICAÇÃO DOS FILTROS
# ============================================================

regioes_filtradas = regioes_mapa.copy()

if regioes_selecionadas:

    regioes_filtradas = regioes_filtradas[
        regioes_filtradas["nome"].isin(
            regioes_selecionadas
        )
    ]

else:

    regioes_filtradas = regioes_filtradas.iloc[0:0]


ocorrencias_filtradas = ocorrencias_mapa.copy()

if "tipo" in ocorrencias_filtradas.columns:

    if tipos_selecionados:

        ocorrencias_filtradas = ocorrencias_filtradas[
            ocorrencias_filtradas["tipo"].isin(
                tipos_selecionados
            )
        ]

    else:

        ocorrencias_filtradas = ocorrencias_filtradas.iloc[0:0]


if "nivel_impacto" in ocorrencias_filtradas.columns:

    if impactos_selecionados:

        ocorrencias_filtradas = ocorrencias_filtradas[
            ocorrencias_filtradas["nivel_impacto"].isin(
                impactos_selecionados
            )
        ]

    else:

        ocorrencias_filtradas = ocorrencias_filtradas.iloc[0:0]


# ============================================================
# 10. INDICADORES GEOGRÁFICOS
# ============================================================

st.subheader("Indicadores geográficos")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Regiões exibidas",
        len(regioes_filtradas)
    )

with col2:

    st.metric(
        "Ocorrências exibidas",
        len(ocorrencias_filtradas)
    )

with col3:

    quantidade_tipos = (
        ocorrencias_filtradas["tipo"].nunique()
        if "tipo" in ocorrencias_filtradas.columns
        else 0
    )

    st.metric(
        "Tipos de ocorrência",
        quantidade_tipos
    )


# ============================================================
# 11. CRIAÇÃO DO MAPA DE NOVA ESPERANÇA
# ============================================================

st.subheader("Mapa territorial de Nova Esperança")

pontos = []

if not regioes_filtradas.empty:

    pontos.extend(
        regioes_filtradas[
            ["latitude", "longitude"]
        ].values.tolist()
    )


if not ocorrencias_filtradas.empty:

    pontos.extend(
        ocorrencias_filtradas[
            ["latitude", "longitude"]
        ].values.tolist()
    )


if not pontos:

    st.warning(
        "Não existem coordenadas válidas para os filtros selecionados."
    )

    st.stop()


latitudes = [
    ponto[0] for ponto in pontos
]

longitudes = [
    ponto[1] for ponto in pontos
]


centro_latitude = sum(latitudes) / len(latitudes)

centro_longitude = sum(longitudes) / len(longitudes)


# Mapa sem base cartográfica real.
# As coordenadas são utilizadas apenas para posicionar
# os elementos da cidade fictícia.

mapa = folium.Map(
    location=[
        centro_latitude,
        centro_longitude
    ],
    zoom_start=11,
    tiles=None,
    control_scale=True
)


# ============================================================
# 12. IDENTIFICAÇÃO VISUAL DA CIDADE
# ============================================================

folium.Marker(
    location=[
        centro_latitude,
        centro_longitude
    ],
    tooltip="Nova Esperança",
    popup="Centro geográfico da cidade fictícia de Nova Esperança",
    icon=folium.Icon(
        color="darkblue",
        icon="home"
    )
).add_to(mapa)


# ============================================================
# 13. MARCADORES DAS REGIÕES
# ============================================================

grupo_regioes = folium.FeatureGroup(
    name="Regiões de Nova Esperança",
    show=True
)


for _, regiao in regioes_filtradas.iterrows():

    nome = regiao.get(
        "nome",
        "Região sem nome"
    )

    zona = regiao.get(
        "zona",
        "Não informada"
    )

    populacao = regiao.get(
        "populacao_estimada",
        "Não informada"
    )

    popup_html = f"""
    <b>Cidade:</b> Nova Esperança<br>
    <b>Região:</b> {nome}<br>
    <b>Zona:</b> {zona}<br>
    <b>População estimada:</b> {populacao}
    """

    folium.CircleMarker(
        location=[
            regiao["latitude"],
            regiao["longitude"]
        ],
        radius=5,
        color="blue",
        fill=True,
        fill_color="blue",
        fill_opacity=0.7,
        popup=folium.Popup(
            popup_html,
            max_width=300
        ),
        tooltip=nome
    ).add_to(grupo_regioes)


grupo_regioes.add_to(mapa)


# ============================================================
# 14. MARCADORES DAS OCORRÊNCIAS
# ============================================================

if not ocorrencias_filtradas.empty:

    coordenadas_ocorrencias = ocorrencias_filtradas[
        ["latitude", "longitude"]
    ].values.tolist()

    grupo_ocorrencias = FastMarkerCluster(
        data=coordenadas_ocorrencias,
        name="Ocorrências",
        show=True
    )

    grupo_ocorrencias.add_to(mapa)


# ============================================================
# 15. ENQUADRAMENTO AUTOMÁTICO
# ============================================================

limite_inferior = [
    min(latitudes),
    min(longitudes)
]

limite_superior = [
    max(latitudes),
    max(longitudes)
]

mapa.fit_bounds(
    [
        limite_inferior,
        limite_superior
    ]
)


# Controle de camadas

folium.LayerControl().add_to(mapa)


# ============================================================
# 16. EXIBIÇÃO DO MAPA
# ============================================================

st_folium(
    mapa,
    width=None,
    height=650,
    returned_objects=[]
)


# ============================================================
# 17. TABELA DE OCORRÊNCIAS
# ============================================================

st.subheader("Detalhamento das ocorrências")

if not ocorrencias_filtradas.empty:

    colunas_exibicao = [
        coluna
        for coluna in [
            "_id",
            "tipo",
            "nivel_impacto",
            "data_hora",
            "linha_id",
            "viagem_id",
            "status"
        ]
        if coluna in ocorrencias_filtradas.columns
    ]

    st.dataframe(
        ocorrencias_filtradas[colunas_exibicao],
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "Nenhuma ocorrência encontrada com os filtros selecionados."
    )


# ============================================================
# 18. RODAPÉ
# ============================================================

st.divider()

st.caption(
    "DataCity Analytics | Nova Esperança — cidade fictícia. "
    "Os pontos representam dados geográficos sintéticos."
)
