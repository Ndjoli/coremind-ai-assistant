import streamlit as st 
from PyPDF2 import PdfReader
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
import os

# 🔐 STEP 1: Load OpenAI API key from Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# ✅ Streamlit page configuration
st.set_page_config(page_title="CoreMind – Internal AI Assistant")

# ✅ Background image (professional Unsplash gradient)
background_url = "https://images.unsplash.com/photo-1508780709619-79562169bc64?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80"
st.markdown(f'''
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url('{background_url}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"], [data-testid="stToolbar"] {{
        background-color: rgba(0,0,0,0);
    }}
    </style>
''', unsafe_allow_html=True)

# 🧠 App title and subtitle
st.markdown("<h1 style='text-align: center; color: #ffffff;'>CoreMind</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #f0f0f0;'>Your Company Knowledge Assistant</h3>", unsafe_allow_html=True)

# 📤 File uploader
uploaded_file = st.file_uploader("Upload Documents (PDF, DOCX, TXT, XLSX)", type=["pdf", "docx", "txt", "xlsx"])

# 📊 Excel text extractor
def extract_text_from_excel(file):
    df = pd.read_excel(file)
    return df.to_string(index=False)

if uploaded_file is not None:
    file_text = ""

    if uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            file_text += page.extract_text() or ""
    elif uploaded_file.name.endswith(".xlsx"):
        file_text = extract_text_from_excel(uploaded_file)
    else:
        file_text = uploaded_file.read().decode("utf-8", errors="ignore")

    # 🧩 Chunk the text for embedding
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(file_text)

    # 🔍 Generate vector embeddings
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(chunks, embedding=embeddings)

    st.success("✅ Document uploaded and processed successfully.")

    # ❓ Ask your question
    st.markdown("<h4 style='color: #ffffff;'>Ask a Question About This File:</h4>", unsafe_allow_html=True)
    user_question = st.text_input("e.g. What does our onboarding policy say about remote work?")

    if st.button("Ask") and user_question:
        llm = ChatOpenAI(model_name="gpt-3.5-turbo")
        qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())
        response = qa_chain.run(user_question)

        # 🖤 Styled answer box
        st.markdown(f'''
        <div style='background-color: #0d1117; padding: 12px; border-radius: 6px;'>
            <span style='color: #39ff14; font-weight: bold;'>Answer:</span><br>
            <span style='color: white; font-weight: bold;'>{response}</span>
        </div>
        ''', unsafe_allow_html=True)

# 🔻 Footer
st.markdown('''
---
<div style='text-align: center; color: #ccc;'>
    <small>Built by Iloyeka Ndjoli | Powered by GPT + FAISS | CoreMind AI Edition</small>
</div>
''', unsafe_allow_html=True)