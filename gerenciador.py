#Login
print("Bem vindo ao GeranciaEChama, entre com seu usuário e senha já cadastrados! ")
def login():
    user_input= input("Usuário: ")
   
    while user_input not in ["admin", "luis"]:
        print("Usuário não cadastrado")
        user_input = input("Usuário: ")

    senha_input=input("Senha: ")

    while True:

        if user_input == "admin" and senha_input=="adminsenha231":
            return "admin"
        
        elif user_input == "luis" and senha_input == "luissenha123":
            return "usuario"
        
        else:
            print("Senha incorreta, tente novamente")
            senha_input = input("Senha: ")


def menu_usuario():
    print(" MENU DO USUÁRIO GERENCIA&CHAMA \n"
    "1 - Abrir um novo chamado\n"
    "2 - Consultar meus chamados\n"
    "3 - Sair")

def menu_adm():
    print(" MENU DO ADMINISTRADOR GERENCIA&CHAMA\n "
    "1 - Ver chamados\n"
    "2 - Alterar status de chamado\n"
    "3 - Cadastrar usuário\n"
    "4 - Listar usuários\n"
    "5 - Sair")

tipo_user = login()

if tipo_user=="admin":
    menu_adm()
    opcao = input("Insira o número da sua opção: ")
    if opcao=="1":
        print("Carregando chamados...")
    elif opcao == "2":
        print("Carregando status...")
    elif opcao == "3":
        print("Carregando cadastro...")
    elif opcao == "4":
        print("Listando usuários...")
    elif opcao == "5":
        print("Saindo...")
    else:
        print("Opção inválida.")


elif tipo_user=="usuario":
    menu_usuario()

    opcao = input("Insira o número da sua opção: ")

    while opcao not in ["1", "2", "3"]:
        print("Opção inválida!")
        opcao = input("Insira o número da sua opção: ")
    if opcao=="1":
        print("Carregando chamado...")
    elif opcao == "2":
        print("Carregando meus chamados...")
    elif opcao=="3":
        print("Saindo...")
        
else:
    print("Erro, recarregue e tente novamente.")
