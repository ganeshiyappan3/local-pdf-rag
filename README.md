# Local PDF RAG

A Retrieval-Augmented Generation (RAG) application that answers questions from PDF documents using a completely local setup.

The project uses **LangChain, Hugging Face embeddings, ChromaDB, and Ollama with Llama 3.2 3B** to retrieve relevant information from a PDF and generate an answer locally.

---

## 🚀 Tech Stack

* Python
* LangChain
* Hugging Face Embeddings
* ChromaDB
* Ollama
* Llama 3.2 3B
* PyPDF

---

## 🔄 RAG Pipeline

```text
PDF Document
     ↓
PDF Loader
     ↓
Text Splitting
     ↓
Hugging Face Embeddings
     ↓
Chroma Vector Database
     ↓
Similarity Search
     ↓
Relevant Context
     ↓
Local LLM (Llama 3.2 3B)
     ↓
Final Answer
```

---

## ⚙️ How It Works

1. Load a PDF document using `PyPDFLoader`.
2. Split the document into smaller chunks using `RecursiveCharacterTextSplitter`.
3. Convert the chunks into vector embeddings using Hugging Face.
4. Store the embeddings in a local Chroma vector database.
5. Retrieve the top 3 relevant chunks based on the user's question.
6. Pass the retrieved context and question to the local Llama 3.2 model.
7. Generate the final answer using the retrieved information.

---

## 📁 Project Structure

```text
local-pdf-rag/
│
├── Data/
│   └── deeplearning.pdf   # Add your own PDF here
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

> **Note:** The sample PDF is not included in this repository because of its file size. To run the project, add your own PDF and name it `deeplearning.pdf` inside the `Data` folder.

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd local-pdf-rag
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🦙 Ollama Setup

This project uses **Ollama** to run the Llama 3.2 3B model locally.

Install Ollama from:

https://ollama.com/

After installation, download the model:

```bash
ollama pull llama3.2:3b
```

Make sure Ollama is running before starting the Python application.

---

## 📄 Add Your PDF

Create a `Data` folder in the project directory:

```text
local-pdf-rag/
└── Data/
```

Place your PDF inside the folder and rename it:

```text
deeplearning.pdf
```

The application expects the following path:

```text
Data/deeplearning.pdf
```

---

## ▶️ Run the Application

Run:

```bash
python main.py
```

The application will:

* Load the PDF
* Split it into chunks
* Generate embeddings
* Create the Chroma vector database
* Retrieve relevant chunks
* Send the retrieved context to Llama 3.2
* Generate the final answer

You can then enter a question about your PDF:

```text
Ask a question about the PDF:
```

---

## 💡 Example

```text
Ask a question about the PDF: What is deep learning?
```

The system retrieves the most relevant document chunks and uses them as context for the local LLM.

If the answer cannot be found in the retrieved context, the application is instructed to respond:

```text
I don't know based on the provided document.
```

---

## 🔐 Local & Privacy-Focused

The project is designed around a local RAG architecture.

* Embeddings are generated locally using Hugging Face.
* The vector database is stored locally using ChromaDB.
* The LLM runs locally through Ollama.
* No external LLM API is required for generating the final answer.

---

## 📌 Key Learning Outcomes

This project demonstrates practical understanding of:

* Retrieval-Augmented Generation (RAG)
* Document loading
* Text chunking
* Vector embeddings
* Vector databases
* Similarity search
* Retrieval
* Context-based prompting
* Local LLM inference
* LangChain integration

---

## 🔮 Future Improvements

Possible improvements include:

* Support for multiple PDF documents
* PDF upload through a web interface
* Streamlit-based user interface
* Conversation memory
* Metadata-based filtering
* Improved retrieval techniques
* Hybrid search
* Reranking retrieved documents

---

## 👨‍💻 Author

Built as a practical project to explore **RAG, LangChain, vector databases, embeddings, and local LLMs**.
