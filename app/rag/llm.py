from llama_index.llms.groq import Groq
from llama_index.core import Settings 
from app.config import settings 

# Settings.llm = Groq(
#     model="llama-3.3-70b-versatile",
#     api_key=settings.groq_api_key
# )

Settings.llm = Groq(
    # model="openai/gpt-oss-20b",
    # model="llama-3.3-70b-versatile",
    # model="meta-llama/llama-4-scout-17b-16e-instruct",
    model="openai/gpt-oss-120b",
    api_key=settings.groq_api_key,    

)