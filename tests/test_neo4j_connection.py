from app.neo4j_client import create_driver

def test_neo4j_connection():
    driver = create_driver()

    try:
        driver.verify_connectivity()
    finally:
        driver.close()
        