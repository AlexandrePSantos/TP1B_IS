from functions.exec_query import execute_query

def cars_to_year_and_eligibility(cars_year, eligibility):
    return execute_query("WITH doc(file) AS (SELECT xml FROM imported_documents) SELECT xpath('//Model[@year<={} and @Eligibility={}]', file) FROM doc".format(cars_year, eligibility))
