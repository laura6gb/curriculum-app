# Curriculum App

Created using **Streamlit**, demonstrates a portfolio application (based on portfolio app from streamlit app gallery https://mehulgupta2016154-resume-builder-streamlit-app-ajmqjx.streamlit.app/) designed to help users create and enhance their CV's. 

## Files
- pages/: Pages navigation supported by Streamlit.
- pdfs/: Contains all files used in te app, incuded CSV and and example .txt for PDF generator.
- pdfs/contant.py: Important file with all static data (text) used in personal portfolio.
- requierements.txt: Generated Streamlit file with all libraries used.

## Features

### 1. **About Me Section**
Displays personal details, skills, achievements, and educational background in an organized and interactive format.

### 2. **CV Text Extraction and Enhancement**
- Upload a PDF CV to extract text using `PyPDF2`.
- Improve the extracted text with AI using the Cohere API.
- Copy or download enhanced text in `.txt` format.

### 3. **PDF CV Generator**
- Generate a professional PDF CV by filling info in simple fields.
- Dynamically formats content with sections like experience, skills, and achievements.
- Downloadable directly from the app (PDF file).

### 4. **Employment Statistics Dashboard**
- Analyze employment rates for various professions in Colombia from 2010 to 2023.
- Filter data by gender and profession.
- View interactive line charts and raw datasets for detailed analysis.
- IMPORTANT: Data displayed is not real, but is based on true databases.

## Technologies Used
- **Python Libraries**: Streamlit, PyPDF2, pandas, fpdf, Cohere API
- **Data Analysis**: Employment data in CSV format
- **API Integration**: Cohere for AI-powered text improvement
- **Visualization**: Interactive line charts and data filters

## Contact
Questions or feedback:
- Email: laura66gb@gmail.com

