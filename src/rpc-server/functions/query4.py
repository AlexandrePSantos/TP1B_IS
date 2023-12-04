from functions.exec_query import execute_query

<<<<<<< Updated upstream
def cars_to_year_and_eligibility(cars_year, eligibility):
    return execute_query("WITH doc(file) AS (SELECT xml FROM imported_documents WHERE is_deleted = 'FALSE') SELECT xpath('//Model[@year<={} and @Eligibility={}]', file) FROM doc".format(cars_year, eligibility))
=======
def cars_to_year_and_eligibility(year, eligibility):
    query = '''SELECT Car.*, eligibility.* 
               FROM Car
               JOIN eligibility ON Car.cafv_ref = eligibility.id 
               WHERE Car.year = "{}" AND eligibility.id = "{}"'''.format(year, eligibility)
    return execute_query(query, fetch=True)


""" def cars_to_year_and_eligibility(cars_year):
    query = '''SELECT Car.* 
               FROM Car 
               WHERE Car.year = "{}"'''.format(cars_year)
    return execute_query(query, fetch=True) """
>>>>>>> Stashed changes
