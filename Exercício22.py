
nome = str(input("Digite seu nome completo: ")).strip()

print("Analisando seu nome...")

print("Seu nome completo em maiusculo é: {}".format(nome.upper()))
print("Seu nome em minusculo é: {}".format(nome.lower()))
print("Seu nome ao todo tem {} letras: ".format(len(nome)- nome.count(" "))) 