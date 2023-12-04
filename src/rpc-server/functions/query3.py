from functions.exec_query import execute_query


<<<<<<< Updated upstream
def frequently_referenced_cars_in_city(city_ref):
    query = '''WITH doc(file) AS (SELECT xml FROM imported_documents WHERE is_deleted = 'FALSE') 
               SELECT xpath('//Car[@city_ref="{}"]/parent::Model/@name', file), 
                      xpath('//Car[@city_ref="{}"]/parent::Model/parent::Maker/@name', file) 
               FROM doc'''.format(city_ref, city_ref)
    return execute_query(query, fetch=True)

=======
def releases_from_car_by_Model(model_name):
    return execute_query("WITH doc(file) AS (SELECT xml FROM imported_documents) SELECT xpath('//Model[@name={}]', file) FROM doc".format(model_name))

def num_car_Maker(maker_name, model_name):
    query = '''WITH doc(file) AS (SELECT xml FROM imported_documents) 
               SELECT xpath('count(//Maker[@name="{}"]/Model[@name="{}"]/Car)', file) FROM doc'''.format(maker_name, model_name)
    return execute_query(query, fetch=True)
>>>>>>> Stashed changes
