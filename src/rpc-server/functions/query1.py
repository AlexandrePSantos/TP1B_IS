from functions.exec_query import execute_query


def releases_from_car_by_id(*car_id):
    return execute_query("with doc(file) as (select xml from imported_documents) SELECT xpath('//Car[@id=%s]', file) FROM doc", (car_id,), fetch=True)
