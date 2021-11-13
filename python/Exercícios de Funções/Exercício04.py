# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def valor(p):
    if p >= 0:
        print(f"O valor P é positivo")
    else:
        print(f"O valor N é negativo")


p = int(input("Digite um número: "))
valor(p)
