from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
from llama_index.core.node_parser import MarkdownNodeParser
import app.rag.embeddings
from app.rag.vector_store import vector_store

reader = SimpleDirectoryReader(
    input_dir="data/unstructured/brochures"
)

documents = reader.load_data()

storage_context = StorageContext.from_defaults(vector_store=vector_store)

node_parser = MarkdownNodeParser()

index = VectorStoreIndex.from_documents(
    documents=documents,
    storage_context=storage_context,
    transformations=[node_parser],
    show_progress=True,
)
print(f"Ingested {len(documents)} documents into pgVector.")