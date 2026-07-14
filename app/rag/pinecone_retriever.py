from llama_index.core import VectorStoreIndex

import app.rag.embeddings  # noqa: F401 — sets Settings.embed_model
from app.rag.pinecone_store import pinecone_vector_store

index = VectorStoreIndex.from_vector_store(vector_store=pinecone_vector_store) 

def retrieve(query : str, top_k : int = 3) : 
    retriever = index.as_retriever(similarity_top_k=top_k)
    return retriever.retrieve(query) 

if __name__ == "__main__" : 
    results = retrieve("What do owners say about fuel economy on the Wagon R?")
    for r in results:
        print(r.score, "-", r.text)   