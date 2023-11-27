import psycopg2

def execute_query(query, params=None, fetch=True):
    try:
        connection = psycopg2.connect(user="is",
                                      password="is",
                                      host="is-db",
                                      port="5432",
                                      database="is")

        cursor = connection.cursor()
        cursor.execute(query, params)

        if fetch:
            result = cursor.fetchall()
            return result
        else:
            connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Failed to execute query:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()