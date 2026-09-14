# ==========================================
# 1. IMPORTS
# ==========================================

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama


# ==========================================
# 2. LOAD PDF
# ==========================================

loader = PyPDFLoader("Data/deeplearning.pdf")

documents = loader.load()

print(f"Number of pages: {len(documents)}")


# ==========================================
# 3. SPLIT PDF INTO CHUNKS
# ==========================================

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print(f"Number of chunks: {len(chunks)}")


# ==========================================
# 4. CREATE EMBEDDING MODEL
# ==========================================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding model loaded")


# ==========================================
# 5. CREATE CHROMA VECTOR DATABASE
# ==========================================

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="Data/chroma_db"
)

print("Vector database created successfully")


# ==========================================
# 6. CREATE RETRIEVER
# ==========================================

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

print("Retriever created")


# ==========================================
# 7. LOAD LOCAL LLM
# ==========================================

llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)

print("Local LLM loaded")


# ==========================================
# 8. ASK USER FOR A QUESTION
# ==========================================

query = input("\nAsk a question about the PDF: ")


# ==========================================
# 9. RETRIEVE RELEVANT DOCUMENTS
# ==========================================

retrieved_docs = retriever.invoke(query)

print("\n==============================")
print("RETRIEVED CHUNKS")
print("==============================")


for i, doc in enumerate(retrieved_docs):

    print(f"\n--- Chunk {i + 1} ---")

    print("Page:", doc.metadata.get("page"))

    print(doc.page_content)


# ==========================================
# 10. CREATE CONTEXT
# ==========================================

context = "\n\n".join(
    doc.page_content
    for doc in retrieved_docs
)


# ==========================================
# 11. CREATE PROMPT
# ==========================================

prompt = f"""
You are a helpful assistant.

Answer the user's question using ONLY the context
provided from the document.

If the answer is not present in the context,
say:

"I don't know based on the provided document."

Context:
{context}

Question:
{query}

Answer:
"""


# ==========================================
# 12. SEND CONTEXT + QUESTION TO LLM
# ==========================================

response = llm.invoke(prompt)


# ==========================================
# 13. DISPLAY FINAL ANSWER
# ==========================================

print("\n==============================")
print("FINAL RAG ANSWER")
print("==============================")

print(response.content)