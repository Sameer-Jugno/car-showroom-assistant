from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # App
    app_name: str = "Car Showroom Assistant"
    environment: str = "development"

    # Postgres / pgVector (Neon / Supabase)
    postgres_url: str

    # Pinecone
    pinecone_api_key: str

    # Redis (Upstash)
    redis_url: str

    # Groq (LLM)
    groq_api_key: str

    # Neo4j (AuraDB)
    neo4j_uri: str
    neo4j_username: str
    neo4j_password: str


settings = Settings()