# 🧠 CoreMind

**Your Company Knowledge Assistant**

CoreMind is an internal AI-powered knowledge assistant designed to help organizations quickly find answers from internal documentation. Upload your company documents (PDF, DOCX, TXT, XLSX), ask natural language questions, and get instant, AI-generated responses — powered by GPT and FAISS.

![CoreMind Preview](coremind_preview.png)

---

## 🚀 Features

- 📄 Supports PDF, DOCX, TXT, and Excel (XLSX) document uploads
- 💡 Asks and answers company-specific questions from uploaded documents
- 🧠 Powered by OpenAI's GPT-3.5 and FAISS vector search
- 🔍 Semantic document chunking and intelligent retrieval
- ✅ Clean, intuitive Streamlit interface with drag-and-drop upload

---

## 🛠️ How It Works

1. **Upload documents** (e.g. company policies, onboarding docs, knowledge bases)
2. CoreMind extracts and splits the content into searchable chunks
3. AI embeddings are generated using OpenAI Embeddings
4. A FAISS vector store indexes the data
5. Users ask questions in natural language
6. The app retrieves the most relevant chunks and feeds them to GPT for an answer

---

## 📂 Tech Stack

- **Python**
- **Streamlit** – for the front-end
- **LangChain** – for retrieval and chaining logic
- **OpenAI** – for embeddings and language modeling
- **FAISS** – for fast vector similarity search
- **PyMuPDF / Python-docx / openpyxl** – for document handling

---

## 🧪 Example Use Cases

- "What does our remote work policy say?"
- "How many leave days are employees entitled to?"
- "When is the next Ocean Innovation Summit?"

---

## 🔐 Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Add your OpenAI API key:

Create a `.env` file in the root folder with the following:

```
OPENAI_API_KEY=your_api_key_here
```

---

---

## 📸 Preview

![CoreMind Preview](coremind_preview.png)

