# 📄 Naive RAG – Document Q&A System

A simple **Retrieval-Augmented Generation (RAG)** application that allows users to upload documents and ask questions about their content. The system retrieves relevant document chunks from a **Weaviate vector database** and uses an **LLM** to generate contextual answers.

## 🚀 Features

* 📂 Upload and process documents
* ✂️ Split documents into smaller chunks
* 🔢 Generate vector embeddings for document chunks
* 🗄️ Store and retrieve embeddings using **Weaviate**
* 🔍 Perform semantic similarity search
* 🤖 Generate answers using an LLM
* 💬 Ask questions based on uploaded documents
* ⚡ Reduces hallucinations by providing relevant document context

## 🏗️ How It Works

```text
User uploads document
        ↓
Document Text Extraction
        ↓
Text Chunking
        ↓
Generate Embeddings
        ↓
Store Chunks + Embeddings
        ↓
     Weaviate
        ↓
User asks a question
        ↓
Question Embedding
        ↓
Semantic Similarity Search
        ↓
Retrieve Relevant Chunks
        ↓
LLM + Retrieved Context
        ↓
Generate Answer
```

## 🛠️ Tech Stack

* **Python**
* **RAG (Retrieval-Augmented Generation)**
* **Weaviate**
* **OpenAI API**
* **Vector Embeddings**
* **Large Language Models (LLMs)**
* **Semantic Search**

## 📁 Project Structure

```text
naive-rag/
│
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
│
├── data/
│   └── documents/
│
├── src/
│   ├── ingestion.py
│   ├── retrieval.py
│   └── rag.py
│
└── ...
```

> The exact structure may vary depending on the implementation.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/saisaritha29/naive-rag.git
cd naive-rag
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
WEAVIATE_URL=your_weaviate_url
WEAVIATE_API_KEY=your_weaviate_api_key
```

**Never commit your `.env` file or API keys to GitHub.**

Use `.env.example` as a template.

## ▶️ Running the Project

After configuring the environment variables, run the application using:

```bash
python <your_main_file>.py
```

Replace `<your_main_file>.py` with the main Python file in the project.

## 🔎 Example

### Document

```text
Machine Learning is a subset of Artificial Intelligence
that enables computers to learn from data without being
explicitly programmed.
```

### User Question

```text
What is Machine Learning?
```

### RAG Process

The system:

1. Converts the question into an embedding.
2. Searches Weaviate for semantically similar document chunks.
3. Retrieves the most relevant chunks.
4. Sends the retrieved context along with the question to the LLM.
5. Generates a context-aware answer.

### Example Answer

```text
Machine Learning is a subset of Artificial Intelligence
that allows computers to learn patterns from data without
being explicitly programmed for every task.
```

## 🧠 What I Learned

Through this project, I explored:

* Fundamentals of **Retrieval-Augmented Generation**
* Document preprocessing and chunking
* Vector embeddings
* Semantic similarity search
* Vector databases
* Weaviate collections and queries
* Connecting LLMs with retrieved context
* Environment variable and API-key management
* Building a basic end-to-end RAG pipeline

## 🔮 Future Improvements

* Support for PDF, DOCX and TXT files
* Web-based document upload interface
* Chat history
* Multiple document collections
* Source citations in generated answers
* Improved chunking strategies
* Hybrid search
* Conversation memory
* Streaming responses
* Authentication and user-specific document storage

## 📌 Project Status

🚧 **Currently under development**

This project is being developed as a learning implementation of a basic Retrieval-Augmented Generation pipeline.

## 👩‍💻 Author

**Sai Saritha**

GitHub: [saisaritha29](https://github.com/saisaritha29)

---

⭐ If you find this project useful, consider giving it a star!
