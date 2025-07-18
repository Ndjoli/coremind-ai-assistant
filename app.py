import streamlit as st
import os
from PyPDF2 import PdfReader
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

# 🔐 Load OpenAI API key from Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# 🌐 Set Streamlit app config
st.set_page_config(page_title="CoreMind AI Assistant", layout="centered")

# 🖼️ Background and Title
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background-image: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e');
            background-size: cover;
            background-position: center;
        }
        [data-testid="stHeader"] {
            background-color: rgba(0,0,0,0);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>🧠 CoreMind: Company Knowledge Assistant</h1>", unsafe_allow_html=True)

# 📤 Upload file
uploaded_file = st.file_uploader("📄 Upload a PDF, Excel (.xlsx), DOCX, or TXT file", type=["pdf", "docx", "txt", "xlsx"])

if uploaded_file:
    raw_text = ""

    # Parse file
    if uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            raw_text += page.extract_text() or ""

    elif uploaded_file.name.endswith(".txt"):
        raw_text = uploaded_file.read().decode("utf-8")

    elif uploaded_file.name.endswith(".docx"):
        import docx2txt
        raw_text = docx2txt.process(uploaded_file)

    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
        raw_text = df.to_csv(index=False)

    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = splitter.split_text(raw_text)

    # Vectorstore setup
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts, embedding=embeddings)
    st.success("✅ File processed successfully.")

    # Ask a question
    user_question = st.text_input("❓ Ask a question about the document:")
    if user_question:
        llm = ChatOpenAI(model_name="gpt-3.5-turbo")
        qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
        result = qa.run(user_question)
        st.markdown(f"<div style='background-color:black; padding:10px; border-radius:5px;'><span style='color:white;'>{result}</span></div>", unsafe_allow_html=True)
