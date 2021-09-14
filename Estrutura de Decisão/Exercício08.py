#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto01 = float(input("Digite o valor do produto:"))
produto02 = float(input("Digite o valor do segundo produto:"))
produto03 = float(input("Digite o valor do terceiro produto:"))

if produto01 < produto02 and produto01 < produto03:
    print("Deve comprar o primeiro produto por ter um valor de: R${}".format(produto01))
elif produto02 < produto01 and produto02 < produto03:
    print("Deve comprar o segundo produto por ter um valor de: R${}".format(produto02))
elif produto03 < produto02 and produto03 < produto01:
    print("Deve comprar o terceiro produto por ter um valor de: R${}".format(produto03))
else:
    print("Todos os valores são iguais!")