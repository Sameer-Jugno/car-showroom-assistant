import asyncio
import time
import app.rag.llm
from llama_index.core import Settings
from llama_index.core.memory import Memory
from llama_index.core.llms import ChatMessage
from app.agents.tools_config import inventory_tool, brochures_retriever_tool, reviews_retriever_tool, find_similar_cars_tool
from llama_index.core.agent.workflow import FunctionAgent
from app.db.redis import redis_client

CACHE_TTL_SECONDS = 3600  # 1 hour

agent = FunctionAgent(
    tools=[inventory_tool, brochures_retriever_tool, reviews_retriever_tool, find_similar_cars_tool],
    llm=Settings.llm,
    system_prompt=(
        "You are a car showroom assistant. Answer ONLY using tool results, "
        "never your own knowledge. If tools lack enough info, say so."
    )
)

_session_memories = {}


def get_memory(session_id: str) -> Memory:
    if session_id not in _session_memories:
        _session_memories[session_id] = Memory.from_defaults(
            session_id=session_id, token_limit=1500
        )
    return _session_memories[session_id]


def _cache_key(session_id: str, query: str) -> str:
    normalized_query = query.strip().lower()
    return f"chat_cache:{session_id}:{normalized_query}"


async def ask_agent(query: str, session_id: str = "default"):
    memory = get_memory(session_id)
    cache_key = _cache_key(session_id, query)

    cached_response = await redis_client.get(cache_key)
    if cached_response is not None:
        memory.put_messages([
            ChatMessage(role="user", content=query),
            ChatMessage(role="assistant", content=cached_response),
        ])
        return cached_response

    response = await agent.run(query, memory=memory)
    response_text = str(response)

    memory.put_messages([
        ChatMessage(role="user", content=query),
        ChatMessage(role="assistant", content=response_text),
    ])

    await redis_client.set(cache_key, response_text, ex=CACHE_TTL_SECONDS)

    return response_text


async def main():
    start1 = time.time()
    response1 = await ask_agent("What's similar to the Maruti 800 AC?", session_id="test1")
    print("First call:", response1)
    print("Time:", time.time() - start1, "seconds")

    start2 = time.time()
    response2 = await ask_agent("What's similar to the Maruti 800 AC?", session_id="test1")
    print("Second call:", response2)
    print("Time:", time.time() - start2, "seconds")


if __name__ == "__main__":
    asyncio.run(main())