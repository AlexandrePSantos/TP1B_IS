import psycopg2
import os
connection = None
cursor = None

try:
    connection = psycopg2.connect(user="is",
                                  password="is",
                                  host="is-db",
                                  port="5432",
                                  database="is")

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM teachers")
    cursor.execute("SELECT * FROM imported_documents")
    
    file_path = os.path.join('/data', 'teste.xml')

    with open(file_path, 'r') as file:
        xml_content = file.read()
    
    cursor.execute("INSERT into imported_documents (file_name, xml) VALUES (%s, %s)", ("teste.xml", xml_content))
    
    connection.commit()

    print("Teachers list:")
    for teacher in cursor:
        print(f" > {teacher[0]}, from {teacher[1]}")

except (Exception, psycopg2.Error) as error:
    print("Failed to fetch data", error)

finally:
    if connection:
        cursor.close()
        connection.close()