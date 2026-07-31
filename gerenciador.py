#Login

def login():
    user="luis"
    senha="luis1"

    user_input = input("Insira o usuário:")
    while user_input != user:
        print("Usuário não encontrado")
        user_input = input("Insira o usuário:")

    senha_input = input("Digite sua senha:")
    while senha_input != senha:
        print("Senha incorreta, tente novamente")
        senha_input = input("Digite sua senha:")
    print("Login realizado!")

login()
#Solicitação de chamado, parte de urgência

def urgencia():
    urgencia_chamado = int(input("Digite 1 para Urgente e 2 para Pode Esperar "))
    while urgencia_chamado not in [1,2]:
        print("Número inválido. Digite apenas 1 ou 2.")
        urgencia_chamado = int(input("Digite 1 para Urgente e 2 para Pode Esperar "))

    if urgencia_chamado == 1:
        print("O setor já foi notificado, logo mais entrarão em contato!")
    elif urgencia_chamado ==2:
        print("Sua solicitação foi enviada, em breve você será atendido!")
urgencia()