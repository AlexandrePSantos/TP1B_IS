import xmlrpc.client

print("Conectando ao servidor...")
server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')

sair = True
while sair:
    print("\n\n--------MENU--------")
    print("1 - Converter csv para xml + validar formato")
    print("2 - Carrega XML para a BD")
    print("3 - Listar ficheiros na BD")
    print("4 - Remove ficheiro da BD")
    print("5 - Query 1")
    print("6 - Query 2")
    print("7 - Query 3")
    print("8 - Query 4")
    print("9 - Query 5")
    print("0 - Sair")

    try:
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "0":
            sair = False
            break
        elif opcao == "1":
            server.convert()
        elif opcao == "2":
            server.loadToDB()
        elif opcao == "3":
            server.listFiles()
        elif opcao == "4":
            server.removeFiles()
        elif opcao == "5":
            # Query 1
            pass
        elif opcao == "6":
            # Query 2
            pass
        elif opcao == "7":
            # Query 3
            pass
        elif opcao == "8":
            # Query 4
            pass
        elif opcao == "9":
            # Query 5
            pass
        else:
            print("Opção inválida. Tente novamente.")
            
    except Exception as e:
        print(f"Erro: {e}")
        sair = False