# 🧠 CoreMind – Your Company Knowledge Assistant

![App Preview](./6b11ab60-fd9e-4cf8-8c09-45461012aef9.png)

CoreMind is an internal AI-powered assistant designed to help teams instantly find information from company documents. Whether it's onboarding manuals, HR policies, or internal SOPs — just upload your file and ask questions in natural language. The app returns direct, intelligent answers pulled from the uploaded content.

---

## 💼 What the App Does

CoreMind turns your company files into a smart Q&A assistant.

- Upload files (PDF, DOCX, TXT, XLSX)
- Ask questions about the content (e.g. _“What does our leave policy say?”_)
- Get accurate answers powered by GPT and semantic search
- Supports multiple document formats and large file sizes
- Great for onboarding, internal knowledge access, and operations

---

## ⚙️ Features

✅ Upload documents (PDF, DOCX, TXT, XLSX)  
✅ Extracts and processes text using LangChain  
✅ Splits text into chunks for semantic vector search (FAISS)  
✅ Uses OpenAI Embeddings + GPT-3.5 for question answering  
✅ Beautiful UI with custom background  
✅ Secure API key handling with Streamlit secrets  
✅ Excel support for tabular policy docs and HR data  

---

## 🧱 Tech Stack

- `Python`
- `Streamlit`
- `LangChain`
- `FAISS`
- `OpenAI GPT (via langchain-openai)`
- `PyPDF2`, `pandas`, and `python-docx` for parsing

---

## 🚀 How to Run It Locally

```bash
# 1. Clone the repo
git clone https://github.com/your-username/coremind-ai-assistant.git
cd coremind-ai-assistant

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your OpenAI key to .streamlit/secrets.toml
# Example secrets.toml
[OPENAI_API_KEY]
OPENAI_API_KEY = "sk-..."

# 4. Run the app
streamlit run app.py
```

---

## 📷 App Preview

![App Preview](./6b11ab60-fd9e-4cf8-8c09-45461012aef9.png)

---

## 👤 Creator

Built by **Iloyeka Ndjoli**  
GitHub: [@Ndjoli](https://github.com/Ndjoli)

---

## 🛡️ License

MIT License – use freely, contribute, and improve it!
