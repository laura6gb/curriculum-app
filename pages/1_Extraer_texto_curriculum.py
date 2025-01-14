import streamlit as st
import cohere
import PyPDF2

st.set_page_config(
    page_title="Extraer texto curriculum", layout="wide", page_icon="book"
)

st.title("Extraer y mejorar texto de Currículum con AI")

st.write(
    "Sube tu curriculum en formato PDF y nos encargaremos de extraer todo el texto del curriculum, si lo deseas podemos mejorarlo con ayuda de Inteligencia Artificial:"
)

uploaded_file = st.file_uploader("Sube tu archivo PDF", type="pdf")

cohere_api_key=st.secrets["COHERE_API_KEY"]
co = cohere.Client(cohere_api_key)

# Process file and extract text
if uploaded_file:
    try:
        # Read PDF
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        all_text = ""

        # Extract text from all pages
        for page in pdf_reader.pages:
            all_text += page.extract_text()

        # Showing text
        if all_text.strip():
            st.subheader("Texto extraído")
            st.text_area("Texto extraído del documento:", all_text, height=300)

            # Improving text with AI
            if st.button("Mejorar texto con IA"):
                with st.spinner("Procesando con IA..."):
                    try:
                        # Call Cohere AI
                        response = co.chat(
                            model="command",
                            message=f"Mejora este texto de curriculum profesionalmente:\n\n{all_text}",
                            max_tokens=500,
                            temperature=0.7,
                        )
                        improved_text = response.text.strip()
                        st.success("Texto mejorado con éxito:")
                        st.text_area("Texto mejorado por IA", improved_text, height=300)

                        # Button: downloading text in .txt
                        st.download_button(
                            "Descargar texto mejorado",
                            improved_text,
                            file_name="texto_mejorado.txt",
                        )
                    except Exception as e:
                        st.error(f"Ocurrió un error al usar la IA: {e}")
        else:
            st.warning(
                "No se pudo extraer texto del archivo. Puede que el PDF esté escaneado o no tenga texto legible."
            )
    except Exception as e:
        st.error(f"Ocurrió un error al procesar el archivo: {e}")

st.sidebar.success("Explora las herramientas que ofrecemos para tu curriculum")
st.sidebar.caption("Wish to connect?")
st.sidebar.write("📧: laura66gb@gmail.com")
