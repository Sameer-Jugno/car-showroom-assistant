import asyncio
import app.rag.llm 
from llama_index.core import Settings 
from app.agents.tools_config import inventory_tool, brochures_retriever_tool, reviews_retriever_tool, find_similar_cars_tool 
from llama_index.core.agent.workflow import FunctionAgent 

agent = FunctionAgent(
    tools=[inventory_tool, brochures_retriever_tool, reviews_retriever_tool, find_similar_cars_tool], 
    llm=Settings.llm,
    system_prompt=(
        "You are a helpful car showroom assistant. You must answer ONLY using "
        "information returned by your tools. Do not use your own general "
        "knowledge about car models, specs, or prices under any circumstances. "
        "If the tools don't return enough information to answer, say so clearly "
        "instead of guessing or filling in gaps."
    )   
)

async def main() : 
    response = await agent.run("What's similar to the Maruti 800 AC?")    
    print(str(response))

if __name__ == "__main__" : 
    asyncio.run(main())