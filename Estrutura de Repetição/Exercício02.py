#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações


while True:
    usario = input("Digite o nome do usuário: ")
    senha = input("Digite a senha do usuário: ")
    if (usario == senha):
        print("")
    else:
        print("Erro, por favor digite as informações novamente! ")
        break




