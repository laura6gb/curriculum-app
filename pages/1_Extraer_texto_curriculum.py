import streamlit as st
import os
from dotenv import load_dotenv
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from langchain_openai import AzureOpenAI

load_dotenv()

# Form Recognizer Keys
fr_endpoint = st.secrets("AZURE_ENDPOINT")
fr_api_key = st.secrets(
    "AZURE_FORM_RECOGNIZER_KEY"
)
document_analysis_client = DocumentAnalysisClient(
    endpoint=fr_endpoint, credential=AzureKeyCredential(fr_api_key)
)

# OpenAi Keys

api_type = "azure"
openai_endpoint = st.secrets("AZURE_OPENAI_ENDPOINT")
openai_api_version = "2024-08-01-preview"
openai_api_key = st.secrets("AZURE_OPENAI_KEY")
deployment_name = st.secrets("AZURE_OPENAI_DEPLOYMENT_NAME")

llm = AzureOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=openai_api_key,
    azure_endpoint=openai_endpoint,
    api_version=openai_api_version,
)

st.set_page_config(
    page_title="Extraer texto curriculum", layout="wide", page_icon="book"
)

st.title("Extraer y mejorar texto de Currículum con AI")
st.write(
    "Sube tu curriculum en formato PDF y nos encargaremos de extraer todo el texto del curriculum, si lo deseas podemos mejorarlo con ayuda de Inteligencia Artificial:"
)

uploaded_file = st.file_uploader("Sube tu archivo PDF", type="pdf")

# Process file and extract text
if uploaded_file:
    try:
        # Binary read and extracting text
        file_bytes = uploaded_file.read()
        with st.spinner("Extrayendo texto del documento..."):
            poller = document_analysis_client.begin_analyze_document(
                model_id="prebuilt-read", document=file_bytes
            )
            result = poller.result()

        all_text = ""
        for page in result.pages:
            for line in page.lines:
                all_text += line.content + "\n"

        # Showing text
        if all_text.strip():
            st.subheader("Texto extraído")
            st.text_area("Texto extraído del documento:", all_text, height=400)

            # Improving text with AI
            if st.button("Mejorar texto con IA"):
                with st.spinner("Procesando con IA..."):
                    try:
                        # Call Azure OpenAI
                        prompt = f"Mejora este texto de curriculum profesionalmente:\n\n{all_text}"
                        response = llm.invoke(prompt)

                        st.success("Texto mejorado con éxito:")
                        st.text_area("Texto mejorado por IA", response, height=300)

                        # Button: downloading text in .txt
                        st.download_button(
                            "Descargar texto mejorado",
                            response,
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
