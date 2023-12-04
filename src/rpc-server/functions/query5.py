from functions.exec_query import execute_query

def cars_with_highest_range():
    query = '''WITH doc(file) AS (SELECT xml FROM imported_documents), 
                      cars AS (SELECT unnest(xpath('//Car[Type/text()="Battery Electric Vehicle (BEV)"]', file)) AS car FROM doc)
               SELECT (xpath('./parent::Model/parent::Maker/@name/text()', car))[1] || ', ' || (xpath('./parent::Model/@name/text()', car))[1] || ', ' || (xpath('@range/text()', car))[1]
               FROM cars
               ORDER BY NULLIF((xpath('@range/text()', car))[1], '')::int DESC'''
    return execute_query(query, fetch=True)