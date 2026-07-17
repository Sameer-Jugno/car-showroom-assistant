from llama_index.core.tools import FunctionTool

from app.tools.inventory_tool import search_inventory
from app.rag.retriever import retrieve as retrieve_brochures
from app.rag.pinecone_retriever import retrieve as retrieve_reviews
from app.tools.graph_tool import find_similar_cars

inventory_tool = FunctionTool.from_defaults(
    fn=search_inventory,
    name="search_inventory",
    description=(
        "Search structured inventory by name, max price, fuel, or transmission. "
        "Use for availability/pricing/filtering questions. Not for opinions or features."
    ),
)

brochures_retriever_tool = FunctionTool.from_defaults(
    fn=retrieve_brochures,
    name="retrieve_brochures",
    description=(
        "Retrieve official spec/feature/financing info from brochures. "
        "Use for factual 'what does this car offer' questions. Not customer opinions."
    ),
)

reviews_retriever_tool = FunctionTool.from_defaults(
    fn=retrieve_reviews,
    name="retrieve_reviews",
    description=(
        "Retrieve real customer reviews about ownership experience/reliability/complaints. "
        "Use for subjective 'is it reliable' or 'what do owners think' questions."
    ),
)

find_similar_cars_tool = FunctionTool.from_defaults(
    fn=find_similar_cars,
    name="find_similar_cars",
    description=(
        "Find cars similar to a given car (same fuel + body type). "
        "Use for 'what's similar to X' or alternative/comparison questions."
    ),
)