import psycopg2

def softDelete(xml_name):
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(user="is",
                                      password="is",
                                      host="is-db",
                                      port="5432",
                                      database="is")

        cursor = connection.cursor()

        cursor.execute("UPDATE imported_documents SET is_deleted = TRUE WHERE file_name = %s", (xml_name,))
        connection.commit()
            
        print("File soft-deleted successfully!")  

    except (Exception, psycopg2.Error) as error:
        print("Failed to soft-delete data", error)

    finally:
        if connection:
            cursor.close()
            connection.close()