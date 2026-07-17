from llama_index.vector_stores.pinecone import PineconeVectorStore 
from app.config import settings 
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key=settings.pinecone_api_key)

INDEX_NAME = "car-showroom-assistant"

if INDEX_NAME not in pc.list_indexes().names() : 
    pc.create_index(
        name= INDEX_NAME, 
        dimension=384, 
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

pinecone_index = pc.Index(INDEX_NAME)

pinecone_vector_store = PineconeVectorStore(
    pinecone_index=pinecone_index
)

# print("Pinecone vector store ready:", pinecone_vector_store)