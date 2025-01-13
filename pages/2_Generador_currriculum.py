import streamlit as st
from fpdf import FPDF


# Formatting PDF text
class PDF(FPDF):

    def chapter_header(self, name, contact):
        self.set_font("Times", "B", 22)

        col_width = 80
        self.set_xy(10, self.get_y())
        self.cell(col_width, 10, name, border=False, ln=False)
        self.ln(0)

        self.set_xy(10 + col_width + 10, self.get_y())
        self.set_font("Times", "", 12)
        self.multi_cell(col_width, 10, contact, border=False)
        self.ln(0)

    def chapter_titles(self, title):
        self.set_font("Times", "B", 12)
        self.cell(0, 10, title, border=False, ln=True)
        self.ln(1)

    def chapter_list(self, item):
        item_list = list(item.split("\n"))
        self.set_font("Times", "", 12)
        for item in item_list:
            self.multi_cell(0, 10, "-" + item, border=False)
            self.ln(0)

    def chapter_body(self, body):
        self.set_font("Times", "", 11)
        self.multi_cell(0, 10, body)
        self.ln(1)


# PDF creator
def generate_pdf(data):
    pdf = PDF()
    pdf.add_page()

    # Add info from user input and formatting
    pdf.chapter_header(data["name"], data["contact"])

    pdf.chapter_titles(data["role"])

    pdf.chapter_titles("Descripción profesional:")
    pdf.chapter_body(data["brief"])

    pdf.chapter_titles("Experiencia laboral:")
    pdf.chapter_body(data["experience"])

    pdf.chapter_titles("Educación y títulos profesionales:")
    pdf.chapter_body(data["education"])

    pdf.chapter_titles("Habilidades y herramientas:")
    pdf.chapter_list(data["skills"])

    pdf.chapter_titles("Logros profesionales y personales:")
    pdf.chapter_list(data["achievements"])

    return pdf


st.set_page_config(
    page_title="Generador de curriculum", layout="wide", page_icon="book"
)


st.title("Generar curriculum PDF")

st.write(
    "Si deseas generar tu curriculum a partir del texto mejorado o tu propio texto, ingresa la siguiente información y te daremos tu curriculum en formato PDF:"
)

# User inputs
name = st.text_input("Nombre completo:")
role = st.text_input("Profesión o estudios:")
contact = st.text_area("Información de contacto (email, teléfono, links adicionales):")
brief = st.text_area("Brief o descripción profesional:")
experience = st.text_area("Experiencia laboral:")
education = st.text_area("Educación y títulos profesionales:")
skills = st.text_area("Habilidades y herramientas:")
achievements = st.text_area("Logros profesionales y personales:")

if st.button("Generar PDF"):
    if not name or not role:
        st.warning("Por favor, completa al menos tu nombre y profesión.")
    else:
        data = {
            "name": name,
            "role": role,
            "contact": contact,
            "brief": brief,
            "experience": experience,
            "education": education,
            "skills": skills,
            "achievements": achievements,
        }

        # Create PDF
        pdf = generate_pdf(data)
        pdf_output = f"{name.replace(' ', '_')}_curriculum.pdf"

        # Saving temporarly
        pdf.output(pdf_output)

        # Download file
        with open(pdf_output, "rb") as pdf_file:
            st.download_button(
                "Descargar Curriculum PDF",
                data=pdf_file,
                file_name=pdf_output,
                mime="application/pdf",
            )

st.sidebar.success("Explora las herramientas que ofrecemos para tu curriculum")
st.sidebar.caption("Wish to connect?")
st.sidebar.write("📧: laura66gb@gmail.com")
