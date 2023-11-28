from functions.exec_query import execute_query


def releases_from_car_by_id(car_id):
    return execute_query("WITH doc(file) AS (SELECT xml FROM imported_documents) SELECT xpath('//Car[@id={}]', file) FROM doc".format(car_id))
