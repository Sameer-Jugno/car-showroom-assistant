from llama_index.core import SimpleDirectoryReader, StorageContext, VectorStoreIndex 
import app.rag.embeddings 
from app.rag.pinecone_store import pinecone_vector_store 
from llama_index.core.node_parser import MarkdownNodeParser

node_parser = MarkdownNodeParser()

reader = SimpleDirectoryReader(
    input_dir="data/unstructured/reviews"
)

documents = reader.load_data()

storage_context = StorageContext.from_defaults(vector_store=pinecone_vector_store)

index = VectorStoreIndex.from_documents(
    documents=documents, 
    storage_context=storage_context, 
    transformations=[node_parser],
    show_progress=True
)

print(f"Ingested {len(documents)} documents into Pinecone.")