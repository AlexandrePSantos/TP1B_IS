from samples import Validate
import psycopg2
import os


# Converte csv para xml e valida o formato
def convert():
    
    pass

# Carrega XML para a BD    
def loadToDB():
    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(user="is",
                                    password="is",
                                    host="is-db",
                                    port="5432",
                                    database="is")
        cursor = connection.cursor()
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

# Lista ficheiros na BD
def listFiles():
    pass
  
# Remove ficheiro da BD (id do ficheiro na tabela)
def removeFiles(id):
    pass
