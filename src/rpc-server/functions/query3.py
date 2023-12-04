from functions.exec_query import execute_query


def frequently_referenced_cars_in_city(city_ref):
    query = '''WITH doc(file) AS (SELECT xml FROM imported_documents WHERE is_deleted = 'FALSE') 
               SELECT xpath('//Car[@city_ref="{}"]/parent::Model/@name', file), 
                      xpath('//Car[@city_ref="{}"]/parent::Model/parent::Maker/@name', file) 
               FROM doc'''.format(city_ref, city_ref)
    return execute_query(query, fetch=True)

