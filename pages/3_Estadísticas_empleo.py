import streamlit as st
import pandas as pd


# Reading CSV
@st.cache_data
def load_data():
    df = pd.read_csv("pdfs\employment_rate_Colombia.csv")
    return df


st.set_page_config(page_title="Estadísticas de Empleo", layout="wide", page_icon="📊")

st.title("Tasa de Empleo por Profesión en Colombia (2010-2023)")
st.write(
    "A continuación puedes observar la tasa de empleo para distintas profesiones a lo largo de los años desde el 2010 al 2023. Si deseas analizar la información detalladamente en el menú lateral podrás filtrar la información de acuerdo al género y profesión concreta:"
)

df = load_data()

st.sidebar.subheader("Filtros")

# Filtering gender
gender_select = st.sidebar.selectbox(
    "Selecciona el género", options=df["Género"].unique()
)

# Filtering career
careers_available = ["Todas"] + list(df["Profesion"].unique())
careers_select = st.sidebar.multiselect(
    "Selecciona las profesiones", options=careers_available, default="Todas"
)

if "Todas" in careers_select:
    careers_filter = df["Profesion"].unique()
else:
    careers_filter = careers_select


df_filtered = df[
    (df["Género"] == gender_select) & (df["Profesion"].isin(careers_filter))
]

# Showing filtered data
st.subheader("Datos de Empleo por Profesión y Género")
with st.expander("Ver base de datos completa"):
    st.write(df)

# Validate and show chart
if not df_filtered.empty:
    df_pivot = df_filtered.pivot(
        index="Año", columns="Profesion", values="Tasa de Empleo"
    )
    st.subheader(f"Gráfico de la Tasa de Empleo por Profesión ({gender_select})")
    st.line_chart(df_pivot)
else:
    st.error("No hay datos disponibles para los filtros seleccionados.")

st.sidebar.success("Explora las herramientas que ofrecemos para tu curriculum")
st.sidebar.caption("Wish to connect?")
st.sidebar.write("📧: laura66gb@gmail.com")
