import llm_utils as llm
import streamlit as st
from PyPDF2 import PdfReader

st.title("Document Summarizer")

pdf = st.file_uploader("Upload pdf file", type="pdf")
if pdf:
    pdf_reader = PdfReader(pdf)
    content = ""
    for page in range(len(pdf_reader.pages)):
        content += pdf_reader.pages[page].extract_text()
    response = llm.summarize_doc(content)
    st.write(response)
    
