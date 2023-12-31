import psycopg2

def importFile(file_path, xml_name):
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(user="is",
                                      password="is",
                                      host="is-db",
                                      port="5432",
                                      database="is")

        cursor = connection.cursor()

        with open(file_path, encoding='utf-8') as file:
            data = file.read()
            cursor.execute("INSERT INTO imported_documents(file_name,xml,is_deleted) VALUES(%s,%s,FALSE)", (xml_name, data))
            connection.commit()
            
            print("File imported successfully!")  

    except (Exception, psycopg2.Error) as error:
        print("Failed to fetch data", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            
            