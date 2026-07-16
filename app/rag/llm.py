from llama_index.llms.groq import Groq
from llama_index.core import Settings 
from app.config import settings 

# Settings.llm = Groq(
#     model="llama-3.3-70b-versatile",
#     api_key=settings.groq_api_key
# )

Settings.llm = Groq(
    model="openai/gpt-oss-20b",
    api_key=settings.groq_api_key,
)