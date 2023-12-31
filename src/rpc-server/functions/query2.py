from functions.exec_query import execute_query


def num_car_Maker(maker_name, model_name):
    query = '''WITH doc(file) AS (SELECT xml FROM imported_documents WHERE is_deleted = 'FALSE') 
               SELECT xpath('count(//Maker[@name="{}"]/Model[@name="{}"]/Car)', file) FROM doc'''.format(maker_name, model_name)
    return execute_query(query, fetch=True)
