from functions.exec_query import execute_query

def cars_of_type_BEV():
    return execute_query("WITH doc(file) AS (SELECT xml FROM imported_documents WHERE is_deleted = 'FALSE') SELECT xpath('count(//Model[@type=\"Battery Electric Vehicle (BEV)\"]/Car)', file) FROM doc")