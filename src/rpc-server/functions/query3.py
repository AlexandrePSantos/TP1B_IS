from functions.exec_query import execute_query


def releases_from_car_by_Model(model_name):
    return execute_query("WITH doc(file) AS (SELECT xml FROM imported_documents) SELECT xpath('//Model[@name={}]', file) FROM doc".format(model_name))
