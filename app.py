import streamlit as st
from pdfs.constant import *
import pandas as pd


st.set_page_config(
    page_title="Laura Galvis's portfolio", layout="wide", page_icon="book"
)

st.sidebar.success("Explora las herramientas que ofrecemos para tu curriculum")

st.header("Conoce un poco acerca de mí")
st.info(
    "En el menú de navegación encontrarás herramientas desarrolladas para facilitarte el desarrollo y creación de tu propio curriculum"
)

st.subheader("Sobre mí")
st.write(info["Brief"])

st.subheader("Habilidades y Herramientas ⚒️")


def skill_tab():
    rows, cols = len(info["skills"]) // skill_col_size, skill_col_size
    skills = iter(info["skills"])
    if len(info["skills"]) % skill_col_size != 0:
        rows += 1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break


with st.spinner(text="Loading section..."):
    skill_tab()

st.subheader("Estudios 📖")

st.dataframe(info["edu"])

st.subheader("Logros 🥇")
achievement_list = "".join(["<li>" + item + "</li>" for item in info["achievements"]])
st.markdown("<ul>" + achievement_list + "</ul>", unsafe_allow_html=True)


st.subheader("Intereses ✍️")
st.write(
    "Me apasionan los libros y la música, así como el arte en general. Sin duda son el medio de expresión más bello que existe. A continuación te comparto algunas de mis recomendaciones:"
)
with st.expander("Libros recomendados"):
    st.write("Algunos de los mejores clásicos de la literatura:")
    df = pd.read_csv("pdfs/books.csv")
    st.dataframe(df)

st.sidebar.caption("Wish to connect?")
st.sidebar.write("📧: laura66gb@gmail.com")
