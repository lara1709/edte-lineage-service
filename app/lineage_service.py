from app.urn_parser import parse_urn
from app.neo4j_client import write_urn_node


def process_urn(driver, value: str) -> str:
    """Validate a URN and store it as a node in Neo4j."""

    canonical_urn = parse_urn(value)
    write_urn_node(driver, canonical_urn)

    return canonical_urn
