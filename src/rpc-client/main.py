import xmlrpc.client

print("Conectando ao servidor...")
server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')

sair = True
while sair:
    print("\n\n--------MENU--------")
    print("1 - Inverter String")
    print("2 - Obter Comprimento da String")
    print("3 - Listar Arquivos")
    print("0 - Sair")

    try:
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "0":
            sair = False
        elif opcao == "1":
            string = input("Digite a string a ser invertida: ")
            resultado = server.string_reverse(string)
            print(f"Resultado: {resultado}")
        elif opcao == "2":
            string = input("Digite a string para obter o comprimento: ")
            resultado = server.string_length(string)
            print(f"Resultado: {resultado}")
        elif opcao == "3":
            # Adicione aqui a lógica para listar arquivos, se necessário
            pass
        else:
            print("Opção inválida. Tente novamente.")
            
    except Exception as e:
        print(f"Erro: {e}")
        sair = False