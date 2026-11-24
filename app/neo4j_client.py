
import os

from neo4j import GraphDatabase


def create_driver():
    """Create a connection to the Neo4j database."""

    uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    username = os.getenv("NEO4J_USERNAME", "neo4j")
    password = os.getenv(
        "NEO4J_PASSWORD",
        "change_this_password_123",
    )

    driver = GraphDatabase.driver(
        uri,
        auth=(username, password),
    )

    return driver


def write_urn_node(driver, urn: str):
    """Create or find a canonical URN node in Neo4j."""

    with driver.session() as session:
        session.run(
            """
            MERGE (n:URN {canonical: $urn})
            """,
            urn=urn,
        )
