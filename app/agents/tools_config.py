from llama_index.core.tools import FunctionTool

from app.tools.inventory_tool import search_inventory
from app.rag.retriever import retrieve as retrieve_brochures
from app.rag.pinecone_retriever import retrieve as retrieve_reviews
from app.tools.graph_tool import find_similar_cars

inventory_tool = FunctionTool.from_defaults(
    fn=search_inventory,
    name="search_inventory",
    description=(
        "Search the car dealership's structured inventory database for cars "
        "matching specific factual criteria such as car name/brand (partial "
        "match), maximum price, fuel type (Petrol, Diesel, CNG, LPG, Electric), "
        "or transmission (Manual, Automatic). Results are limited to a small "
        "number of matches by default. Use this tool when the user asks about "
        "availability, pricing, or wants to filter/list cars by concrete "
        "attributes — e.g. 'show me automatic cars under 500000' or 'what "
        "diesel cars do you have' or 'price of Maruti Suzuki cars'. Do NOT use "
        "this for questions about how a car feels to drive, its features, or "
        "owner opinions — use the other tools for that."
    )
)

brochures_retriever_tool = FunctionTool.from_defaults(
    fn=retrieve_brochures,
    name="retrieve_brochures",
    description=("Retrieve official specification and feature information from car "
        "brochures — covers technical specs, trim levels, interior/exterior "
        "features, safety systems, maintenance schedules, and financing "
        "options. Use this tool when the user asks factual 'what does this "
        "car offer' style questions — e.g. 'what features does the Creta "
        "have' or 'what's the warranty on the Amaze'. This is manufacturer/ "
        "dealership-provided information, not customer opinions.")
)

reviews_retriever_tool = FunctionTool.from_defaults(
    fn=retrieve_reviews,
    name="retrieve_reviews",
    description=("Retrieve real customer reviews and testimonials about a car's actual "
        "ownership experience — covers reliability, common complaints, "
        "fuel economy in real-world use, and overall satisfaction. Use this "
        "tool when the user asks subjective or experience-based questions — "
        "e.g. 'is the Amaze reliable' or 'what do owners think of the Wagon "
        "R'. This is customer opinion, not official specifications.")  
)

find_similar_cars_tool = FunctionTool.from_defaults(
    fn=find_similar_cars,
    name="find_similar_cars",
    description=(
        "Find cars similar to a given car, based on shared fuel type and "
        "body type (e.g. two SUVs that are both diesel). Use this tool when "
        "the user explicitly asks for alternatives or comparisons — e.g. "
        "'what's similar to the Creta' or 'show me other options like the "
        "Swift'. Takes a car name as input."
    )
)

