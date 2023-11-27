import psycopg2

def execute_query(query, params=None, fetch=False):
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(user="is",
                                      password="is",
                                      host="is-db",
                                      port="5432",
                                      database="is")

        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        
        if fetch:
            return cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        print("Failed to fetch data", error)

    finally:
        if connection:
            cursor.close()
            connection.close()