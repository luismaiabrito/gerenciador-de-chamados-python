#Login
#Lista de funcionalidades admin: Ver chamados, alterar status, cadastrar user, listar users
#Lista funcionalidades user; Abrir new chamado, consultar meus chamados
print("Bem vindo ao Gerencia&Chama, entre com seu usuário e senha já cadastrados! ")

chamados=[]

def login():
    user_input= input("Usuário: ")
   
    while user_input not in ["mestre", "luis"]:
        print("Usuário não cadastrado")
        user_input = input("Usuário: ")

    senha_input=input("Senha: ")

    while True:

        if user_input == "mestre" and senha_input=="eusouomestredosmagos":
            return "admin"
        
        elif user_input == "luis" and senha_input == "senhacorreta":
            return "usuario"
        
        else:
            print("Senha incorreta, tente novamente")
            senha_input = input("Senha: ")

def menu_usuario():
    while True:
        print("MENU DO USUÁRIO GERENCIA&CHAMA \n")
        print("1 - Abrir um novo chamado \n")
        print("2 - Consultar meus chamados \n")
        print("3 - Sair")

        opcao = input("Insira o número da sua opção: ")

        while opcao not in ["1", "2", "3"]:
            print("Opção inválida!")
            opcao = input("Insira o número da sua opção: ")

        if opcao == "1":
            print("Carregando chamado...")
            abrir_cham()

        elif opcao == "2":
            print("Carregando meus chamados...")

        elif opcao == "3":
            print("Saindo...")
            break

def menu_adm():
    while True:
        print(" MENU DO ADMINISTRADOR GERENCIA&CHAMA\n "
        "1 - Ver chamados\n"
        "2 - Alterar status de chamado\n"
        "3 - Cadastrar usuário\n"
        "4 - Listar usuários\n"
        "5 - Sair")

        opcao = input("Escolha o que deseja inserindo o número da sua opção: ")

        while opcao not in ["1", "2", "3", "4", "5"]:
            print("Opção inválida!")
            opcao = input("Insira o número da sua opção: ")
        
        if opcao == "1":
            for chamado in chamados:
                print(chamado["id"])
                print(chamado["titulo"])
                print(chamado["descricao"])
                print(chamado["prioridade"])
                print(chamado["status"])

        
        elif opcao == "2":
            print("Carregando status de chamdos...")

        elif opcao == "3":
            print("Entrando em área de cadastro...")

        elif opcao == "4":
            print("Listando users...")

        elif opcao == "5":
            print("Saindo...")
            break

def abrir_cham():

    titulo_chamado = input("Título: ")
    descricao_chamado = input("Descreva: ")
    prioridade_chamado = input("Prioridade (Urgente, necessário): ")

    chamado = {
        "id": len(chamados) + 1,
        "titulo": titulo_chamado,
        "descricao": descricao_chamado,
        "prioridade": prioridade_chamado,
        "status": "Aberto"

    }
    chamados.append(chamado)
    print("Chamado cadastrado com sucesso!")
while True:
    tipo_user = login()

    if tipo_user == "admin":
        menu_adm()

    elif tipo_user == "usuario":
        menu_usuario()

    else:
        print("Erro, recarregue e tente novamente.")
    print("Deseja entrar novamente no Gerencia&Chama?\n 1 - Sim \n 2 - Encerrar")
    opcao_encerra = input("Escolha a opção inserindo seu número correspondente: ")

    while opcao_encerra not in ["1", "2"]:
        print("Opção inválida!")
        opcao_encerra = input("Escolha a opção inserindo seu número correspondente: ")
    if opcao_encerra == "1":
        print("Voltando para login...")
    elif opcao_encerra =="2":
        print("Encerrando por hoje...")
        break
