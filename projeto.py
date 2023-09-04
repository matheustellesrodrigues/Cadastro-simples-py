Cadastro = []
while True: 
    print("1 - Realizar Cadastro: ")
    print("2 - Listar Cadastro: ")
    print("3 - Sair: ")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        cpf = int(input("Digite seu cpf: "))

        cadastro = {"nome": nome, "idade": idade, "cpf": cpf}
        Cadastro.append(cadastro)
    
    if opcao == 2: 
        for cadastro in Cadastro:
            print(cadastro)
    
    if opcao == 3:
        print("até logo")
        break
    