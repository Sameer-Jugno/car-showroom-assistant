from llama_index.vector_stores.postgres import PGVectorStore

from app.config import settings
from sqlalchemy.engine import make_url

url = make_url(
    settings.postgres_url.replace("postgresql://", "postgresql+psycopg2://", 1).split("?")[0]
)

vector_store = PGVectorStore.from_params(
    database=url.database,
    host=url.host,
    password=url.password,
    port=url.port or 5432,
    user=url.username,
    table_name="brochure_chunks",
    embed_dim=384,
)
