from app.db.neo4j import driver

FIND_SIMILAR_QUERY = """
MATCH (c:Car {name: $car_name})-[:SIMILAR_TO]->(similar:Car)
RETURN similar.name AS name
"""


def find_similar_cars(car_name: str):
    with driver.session() as session:
        result = session.run(FIND_SIMILAR_QUERY, car_name=car_name)
        return [record["name"] for record in result]