from llama_index.llms.groq import Groq
from llama_index.core import Settings

from app.config import settings

# Model history: llama3-70b-8192 (deprecated) -> llama-3.3-70b-versatile
# (intermittent malformed tool-call errors) -> openai/gpt-oss-20b (too-tight
# TPM limit) -> llama-4-scout-17b-16e-instruct (deprecated) ->
# openai/gpt-oss-120b (current, stable choice)
Settings.llm = Groq(
    model="openai/gpt-oss-120b",
    api_key=settings.groq_api_key,
)