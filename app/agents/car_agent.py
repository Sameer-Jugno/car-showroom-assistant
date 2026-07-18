import asyncio
import app.rag.llm 
from llama_index.core import Settings 
from app.agents.tools_config import inventory_tool, brochures_retriever_tool, reviews_retriever_tool, find_similar_cars_tool 
from llama_index.core.agent.workflow import FunctionAgent 

agent = FunctionAgent(
    tools=[inventory_tool, brochures_retriever_tool, reviews_retriever_tool, find_similar_cars_tool], 
    llm=Settings.llm,
    system_prompt=(
        "You are a car showroom assistant. Answer ONLY using tool results, "
        "never your own knowledge. If tools lack enough info, say so."
    )   
)

async def main() : 
    response = await agent.run("Is the Hyundai Creta reliable, and what's similar to it?")
    print(str(response))

if __name__ == "__main__" : 
    asyncio.run(main())