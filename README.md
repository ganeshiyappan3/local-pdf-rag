# Local RAG Project

A Retrieval-Augmented Generation (RAG) application that answers questions
from a PDF document using a completely local setup.

## Tech Stack

- Python
- LangChain
- Hugging Face Embeddings
- ChromaDB
- Ollama
- Llama 3.2 3B

## RAG Pipeline

PDF
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

## How It Works

1. Load the PDF document.
2. Split the document into smaller chunks.
3. Convert the chunks into embeddings.
4. Store the embeddings in a local Chroma vector database.
5. Retrieve the most relevant chunks for the user's question.
6. Pass the retrieved context to the local Llama model.
7. Generate the final answer.

## Project Structure

RAG/
├── Data/
│   └── deeplearning.pdf
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

## Setup

Install the required Python packages:

```bash
pip install -r requirements.txt
python main.py