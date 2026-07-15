# scripts/build_graph.py

from app.db.neo4j import driver

cars = [
    {
        "name": "Maruti 800 AC",
        "brand": "Maruti",
        "fuel": "Petrol",
        "body_type": "Hatchback",
    },
    {
        "name": "Maruti Wagon R LXI",
        "brand": "Maruti",
        "fuel": "Petrol",
        "body_type": "Hatchback",
    },
    {
        "name": "Hyundai Verna 1.6 SX",
        "brand": "Hyundai",
        "fuel": "Diesel",
        "body_type": "Sedan",
    },
    {
        "name": "Honda Amaze VX i-DTEC",
        "brand": "Honda",
        "fuel": "Diesel",
        "body_type": "Sedan",
    },
    {
        "name": "Hyundai Creta 1.6 VTVT S",
        "brand": "Hyundai",
        "fuel": "Petrol",
        "body_type": "SUV",
    },
]

CREATE_CAR_QUERY = """
MERGE (c:Car {name: $name})
MERGE (b:Brand {name: $brand})
MERGE (f:FuelType {name: $fuel})
MERGE (t:BodyType {name: $body_type})
MERGE (c)-[:MADE_BY]->(b)
MERGE (c)-[:USES_FUEL]->(f)
MERGE (c)-[:IS_TYPE]->(t)
"""

SIMILAR_TO_QUERY = """
MATCH (c1:Car)-[:IS_TYPE]->(t:BodyType)<-[:IS_TYPE]-(c2:Car)
MATCH (c1:Car)-[:USES_FUEL]->(f:FuelType)<-[:USES_FUEL]-(c2:Car)
WHERE c1.name < c2.name
MERGE (c1)-[:SIMILAR_TO]->(c2)
MERGE (c2)-[:SIMILAR_TO]->(c1)
"""

with driver.session() as session:
    for car in cars:
        session.run(CREATE_CAR_QUERY, car)

    session.run(SIMILAR_TO_QUERY)

print(f"Built graph: {len(cars)} cars, brands, fuel types, body types, and similarity links.")