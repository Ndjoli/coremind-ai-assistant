# 🧠 CoreMind – Internal AI Assistant

**CoreMind** is a smart internal assistant designed to help teams instantly access company knowledge locked in documents. Whether it's onboarding manuals, project reports, HR policies, or training guides, CoreMind lets you upload a file and ask natural language questions — and it gives you instant answers.

It uses **OpenAI GPT**, **LangChain**, and **FAISS vector search** to break down and understand documents like PDFs, Excel sheets, and plain text files. It’s like ChatGPT — but for your internal company files.

---

## 💡 What the App Does

1. 📤 Upload a document (PDF, TXT, or Excel).
2. 🧠 CoreMind breaks the file into chunks and converts them into embeddings (via LangChain + FAISS).
3. 🤖 You type a question — like “When is the next team event?” — and the app searches the document for the best answer using GPT-3.5.
4. ✅ It returns the answer in a clean, professional layout.

It’s perfect for:
- Searching onboarding manuals
- Querying policy documents
- Accessing internal knowledge without digging through files

---

## 🚀 Features

- 📤 Upload documents (PDF, TXT, XLSX)
- 🔎 Ask questions and receive smart answers from the file
- 🤖 Powered by GPT-3.5 + FAISS for semantic retrieval
- 🧱 Uses LangChain for chunking and retrieval pipeline
- 🌐 Beautiful UI with a professional background
- 🔐 API Key stored securely via environment variable

---

## 🛠 Tech Stack

| Layer      | Tools                     |
|------------|----------------------------|
| Backend    | Python, LangChain, FAISS   |
| AI Model   | OpenAI GPT-3.5             |
| Frontend   | Streamlit                  |
| File Types | PDF, TXT, Excel (.xlsx)    |

---

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/coremind-ai-assistant.git
cd coremind-ai-assistant
pip install -r requirements.txt
```

---

## 🔐 Set API Key

Create a `.env` file in the root directory and add your OpenAI key:

```bash
OPENAI_API_KEY=sk-...
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open in browser: `http://localhost:8501`

---

## 🧪 Sample Documents

You can test the app with files inside the `sample_docs/` folder:
- `FutureTech_Onboarding.pdf`
- `CRM_Project_Status_Report.txt`

---

## 📸 Screenshot
![CoreMind Preview](coremind_preview.png)

