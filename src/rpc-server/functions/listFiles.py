import psycopg2

def listFiles():
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(user="is",
                                      password="is",
                                      host="is-db",
                                      port="5432",
                                      database="is")

        cursor = connection.cursor()
        cursor.execute("SELECT id, file_name, created_on, is_deleted FROM imported_documents")
        connection.commit()
        
        print("Files in the database:")
        return cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        print("Failed to fetch data", error)

    finally:
        if connection:
            cursor.close()
            connection.close()