import streamlit as st
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Form Recognizer Keys
fr_endpoint = st.secrets["AZURE_ENDPOINT"]
fr_api_key = st.secrets[AZURE_FORM_RECOGNIZER_KEY"]
document_analysis_client = DocumentAnalysisClient(
    endpoint=fr_endpoint, credential=AzureKeyCredential(fr_api_key)
)

# OpenAi Keys
openai_service = st.secrets["AZURE_OPENAI_SERVICE"]
openai_api_version = "2024-08-01-preview"
openai_api_key = st.secrets["AZURE_OPENAI_KEY"]
deployment_name = st.secrets["AZURE_OPENAI_DEPLOYMENT_NAME"]

llm = AzureChatOpenAI(
    azure_deployment="gpt-4o-mini",
    temperature=0,
    api_key=openai_api_key,
    azure_endpoint=f"https://{openai_service}.openai.azure.com/",
    api_version=openai_api_version,
)


def PDF_text_extract(file_bytes):
    try:
        poller = document_analysis_client.begin_analyze_document(
            model_id="prebuilt-read", document=file_bytes
        )
        result = poller.result()

        all_text = ""
        for page in result.pages:
            for line in page.lines:
                all_text += line.content + "\n"
        return all_text.strip()
    except Exception as e:
        raise ValueError(f"Error al procesar el archivo: {e}")


def formatter_AI(all_text):
    try:
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "Eres un asistente especializado en aplicar formato markdown y orden a un texto.",
                ),
                (
                    "human",
                    f"Ordena este texto de CV y aplicale formato markdown, solo incluye el texto sin comentarios adicionales:\n\n{all_text}",
                ),
            ]
        )
        # Configura el input
        input_data = {"text": all_text}
        # Combina el prompt con el LLM y ejecuta
        runnable = prompt | llm
        response = runnable.invoke(input_data)
        formatted_text = (
            response.content if hasattr(response, "content") else str(response)
        )
        return formatted_text
    except Exception as e:
        raise ValueError(f"Error al procesar el texto con IA: {e}")


def improverAI_cv(all_text):
    try:
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "Eres un asistente especializado en mejorar currículums profesionales.",
                ),
                (
                    "human",
                    f"Mejora este texto de currículum profesionalmente respetando el formato markdown, solo incluye el texto mejorado sin comentarios adicionales:\n\n{all_text}",
                ),
            ]
        )
        # Configura el input
        input_data = {"cv": all_text}
        # Combina el prompt con el LLM y ejecuta
        runnable = prompt | llm
        response = runnable.invoke(input_data)
        improved_text = (
            response.content if hasattr(response, "content") else str(response)
        )
        return improved_text
    except Exception as e:
        raise ValueError(f"Error al procesar el texto con IA: {e}")


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
        # Leer archivo y extraer texto con Form Recognizer
        file_bytes = uploaded_file.read()
        with st.spinner("Extrayendo texto del documento..."):
            extracted_text = formatter_AI(PDF_text_extract(file_bytes))
        if extracted_text:
            st.subheader("Texto extraído")
            st.text_area("Texto extraído del documento:", extracted_text, height=300)

            # Mejorar texto con IA
            if st.button("Mejorar texto con IA"):
                with st.spinner("Procesando con IA..."):
                    try:
                        improved_text = improverAI_cv(extracted_text)
                        # Extraer texto de la respuesta
                        st.success("Texto mejorado con éxito:")
                        st.subheader("Texto mejorado con OpenAI:")
                        st.markdown(improved_text)

                        st.download_button(
                            "Descargar texto mejorado",
                            improved_text,
                            file_name="texto_mejorado.txt",
                        )
                    except Exception as e:
                        st.error(f"Ocurrió un error al procesar con IA: {e}")
        else:
            st.warning(
                "No se pudo extraer texto del archivo. Puede que el PDF esté escaneado o no tenga texto legible."
            )
    except Exception as e:
        st.error(f"Ocurrió un error al procesar el archivo: {e}")

st.sidebar.success("Explora las herramientas que ofrecemos para tu curriculum")
st.sidebar.caption("Wish to connect?")
st.sidebar.write("📧: laura66gb@gmail.com")
