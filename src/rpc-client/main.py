import xmlrpc.client

print("Conectando ao servidor...")
server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000', allow_none = True)

while True:
    print("\n\n-    MENU    -")
    print("1 - Convert CSV file")
    print("2 - Validate XML file")
    print("3 - Import XML file")
    print("4 - Query 1")
    print("5 - Query 2")
    print("6 - Query 3")
    print("7 - Query 4")
    print("8 - Query 5")
    print("0 - Exit")

    op = str(input("Select an option: "))

    if (op == '1'):
        print("Convert CSV file to XML")
        # server.converter()

    elif (op == '2'):
        print("Validate XML file with Schema")
        output = server.validateFile()
        print(output)

    elif (op == '3'):
        print("Import XML file to Database")
        result = server.importFile('/data/result.xml', input("File name to store in the database: "))
        print(result)

    elif (op == '4'):
        pass

    elif (op == '5'):
        pass

    elif (op == '6'):
        pass

    elif (op == '7'):
        pass
    
    elif (op == '8'):
        pass
        # cities = server.query3()
        # print(cities)


    elif (op == '0'):
        print("Exiting...")
        break

    else:
        print("Invalid option")
