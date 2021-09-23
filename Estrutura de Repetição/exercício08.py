#Faça um programa que leia 5 números e informe a soma e a média dos números

soma = 0
for i in range(5):
    numero = float(input("Digite um número: "))
    soma += numero

resultado = numero + soma
media = soma/5
print("A soma é {resultado}".format(resultado))
print("A média é {:.2f}".format(media))