#Faça um programa que leia 5 números e informe a soma e a média dos números

soma = 0
for i in range(5):
    numero = float(input("Digite um número: "))
    soma += numero

print("A soma dos números são: {:.2f} ".format(soma))
media = soma/5
print("A média é {:.2f}".format(media))