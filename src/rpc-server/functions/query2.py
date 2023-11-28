from functions.exec_query import execute_query


def num_car_Maker(maker_name):
    return execute_query("WITH doc(file) AS (SELECT xml FROM imported_documents) SELECT xpath('count(//Car/Maker[.={0}])', file) FROM doc".format(maker_name))