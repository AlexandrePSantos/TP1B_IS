""" from functions.exec_query import execute_query

def num_car_Maker(num_car):
    return execute_query("WITH doc(file) AS (SELECT xml FROM imported_documents) SELECT xpath('//Marker[@name={}]', file) AS Marker, count(xpath('//Model[@name={}]', file)) AS Model, SELECT xpath('//Marker[@name={}]', file) AS Marker, count(xpath('//Car[@id={}]', file)) AS car_count FROM doc".format(num_car))
 """
from functions.exec_query import execute_query

def num_car_Maker(num_car):
    query = """
        WITH doc(file) AS (
            SELECT xml FROM imported_documents
        )
        SELECT
            xpath('//Marker[@name="{}"]', file) AS Marker,
            count(xpath('//Model[@name="{}"]', file)) AS Model,
            xpath('//Model[@name="{}"]', file) AS Marker,
            count(xpath('//Car[@id="{}"]', file)) AS car_count
        FROM doc
    """.format(num_car, num_car, num_car, num_car)

    return execute_query(query)
