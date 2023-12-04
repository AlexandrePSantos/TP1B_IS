from functions.exec_query import execute_query

def cars_before_year_and_eligibility(cars_year, eligibility):
    return execute_query("WITH doc(file) AS (SELECT xml FROM imported_documents WHERE is_deleted = 'FALSE') SELECT xpath('//Model[@year<=\"{}\" and @cafv_ref=\"{}\"]', file) FROM doc".format(cars_year, eligibility))
    