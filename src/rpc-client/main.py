import xmlrpc.client

print("Conectando ao servidor...")
server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000', allow_none = True)

while True:
    print("\n\n-    MENU    -")
    print("1 - Convert CSV file")
    print("2 - Validate XML file")
    print("3 - Import XML file")
    print("4 - List files from the database")
    print("5 - Soft-delete file from the database")
    print("6 - Search car by id")
    print("0 - Exit")

    op = str(input("Select an option: "))

    if (op == '1'):
        print("Convert CSV file to XML")
        server.to_xml_str()
        
    elif (op == '2'):
        print("Validate XML file with Schema")
        output = server.validateFile()
        print(output)

    elif (op == '3'):
        print("Import XML file to Database")
        server.importFile('/data/result.xml', input("File name to store in the database: "))
    
    elif (op == '4'):
        print("List files from the database")
        output = server.listFiles()
        print(output)
        
    elif (op == '5'):
        print("Soft-delete file from the database")
        server.softDelete(input("File name to soft-delete from the database: "))
        
    elif (op == '6'):
        print("Search car by id")
        output = server.releases_from_car_by_id(input("Id of the car you want to search for: "))
        print(output)
 
    elif (op == '0'):
        print("Exiting...")
        break

    else:
        print("Invalid option")
