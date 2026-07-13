from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5",
    show_progress_bar=True,
)


def generate_embeddings(docs):
    embeddings = []
    for doc in docs:
        embedding = Settings.embed_model.get_text_embedding(doc.text)
        embeddings.append(embedding)
    return embeddings