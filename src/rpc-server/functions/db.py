import psycopg2
import os

def load():
    try:
        connection = psycopg2.connect(user="is",
                                        password="is",
                                        host="is-db",
                                        port="5432",
                                        database="is")

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM imported_documents")

        file_path = os.path.join('/data', 'teste.xml')

        with open(file_path, 'r') as file:
            xml_content = file.read()

        cursor.execute("INSERT into imported_documents (file_name, xml) VALUES (%s, %s)", ("teste.xml", xml_content))

        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Failed to fetch data", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

def list():
    try:
        connection = psycopg2.connect(user="is",
                                        password="is",
                                        host="is-db",
                                        port="5432",
                                        database="is")

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM imported_documents")

        print("The number of parts: ", cursor.rowcount)
        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone()

    except (Exception, psycopg2.Error) as error:
        print("Failed to fetch data", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            
def remove(id):
    try:
        connection = psycopg2.connect(user="is",
                                        password="is",
                                        host="is-db",
                                        port="5432",
                                        database="is")

        cursor = connection.cursor()
        cursor.execute("DELETE FROM imported_documents WHERE id = %s", (id,))

        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Failed to fetch data", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            