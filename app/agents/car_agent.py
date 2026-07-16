import asyncio
import app.rag.llm 
from llama_index.core import Settings 
from app.agents.tools_config import inventory_tool, brochures_retriever_tool, reviews_retriever_tool, find_similar_cars_tool 
from llama_index.core.agent.workflow import FunctionAgent 

agent = FunctionAgent(
    tools=[inventory_tool, brochures_retriever_tool, reviews_retriever_tool, find_similar_cars_tool], 
    llm=Settings.llm,
    system_prompt="You are helpful car showroom assistant with strong knowledge of cars and their specifications."
)

async def main() : 
    response = await agent.run("what is price of maruti suzuki ? ")
    print(str(response))

if __name__ == "__main__" : 
    asyncio.run(main())