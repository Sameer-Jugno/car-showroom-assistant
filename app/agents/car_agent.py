import asyncio
import json
import app.rag.llm
from llama_index.core import Settings
from llama_index.core.memory import Memory
from llama_index.core.llms import ChatMessage
from app.agents.tools_config import inventory_tool, brochures_retriever_tool, reviews_retriever_tool, find_similar_cars_tool
from llama_index.core.agent.workflow import FunctionAgent
from app.db.redis import redis_client

CACHE_TTL_SECONDS = 3600          # 1 hour, for cached responses
HISTORY_TTL_SECONDS = 86400       # 24 hours, for persisted conversation history

agent = FunctionAgent(
    tools=[inventory_tool, brochures_retriever_tool, reviews_retriever_tool, find_similar_cars_tool],
    llm=Settings.llm,
    system_prompt=(
        "You are a car showroom assistant. Answer ONLY using tool results, "
        "never your own knowledge. If tools lack enough info, say so."
    )
)

_session_memories = {}


def _history_key(session_id: str) -> str:
    return f"chat_history:{session_id}"


async def _load_history_from_redis(session_id: str):
    raw = await redis_client.get(_history_key(session_id))
    if raw is None:
        return []
    data = json.loads(raw)
    return [ChatMessage(role=item["role"], content=item["content"]) for item in data]


async def _save_history_to_redis(session_id: str, messages):
    data = [{"role": str(msg.role.value), "content": str(msg.content)} for msg in messages]
    await redis_client.set(_history_key(session_id), json.dumps(data), ex=HISTORY_TTL_SECONDS)


async def get_memory(session_id: str) -> Memory:
    if session_id not in _session_memories:
        memory = Memory.from_defaults(session_id=session_id, token_limit=1500)

        restored_messages = await _load_history_from_redis(session_id)
        if restored_messages:
            memory.put_messages(restored_messages)

        _session_memories[session_id] = memory

    return _session_memories[session_id]


def _cache_key(session_id: str, query: str) -> str:
    normalized_query = query.strip().lower()
    return f"chat_cache:{session_id}:{normalized_query}"


async def ask_agent(query: str, session_id: str = "default"):
    memory = await get_memory(session_id)
    cache_key = _cache_key(session_id, query)

    cached_response = await redis_client.get(cache_key)
    if cached_response is not None:
        memory.put_messages([
            ChatMessage(role="user", content=query),
            ChatMessage(role="assistant", content=cached_response),
        ])
        await _save_history_to_redis(session_id, memory.get())
        return cached_response

    response = await agent.run(query, memory=memory)
    response_text = str(response)

    memory.put_messages([
        ChatMessage(role="user", content=query),
        ChatMessage(role="assistant", content=response_text),
    ])
    await _save_history_to_redis(session_id, memory.get())

    await redis_client.set(cache_key, response_text, ex=CACHE_TTL_SECONDS)

    return response_text

async def main():
    response = await ask_agent("What's similar to the Maruti 800 AC?", session_id="test1")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())