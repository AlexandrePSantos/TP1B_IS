import xml.etree.ElementTree as ET

def query2():
    query = """
    WITH ord_models AS (
        SELECT DISTINCT Maker, Model
        FROM imported_documents
    )
    SELECT Maker, Model
    FROM ord_models
    ORDER BY Maker ASC, Model ASC
    """
    return query
