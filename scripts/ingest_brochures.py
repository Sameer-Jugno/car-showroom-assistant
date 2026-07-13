from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
import app.rag.embeddings 
from app.rag.vector_store import vector_store

reader = SimpleDirectoryReader(
    input_dir="data/unstructured/brochures"
)

documents = reader.load_data() 

storage_context = StorageContext.from_defaults(vector_store=vector_store) 

index = VectorStoreIndex.from_documents(
    documents=documents, 
    storage_context=storage_context,
    show_progress=True
)
print(f"Ingested {len(documents)} documents into pgVector.")
