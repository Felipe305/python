#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

tamanho = float(input("Digite quantos metros quadrados sera pintado?"))
litros = tamanho / 3
latas = int(litros / 18)

if (litros % 18 != 0):
    latas +=1

    print("Você devera compras latas {}".format(latas))
    print("O valor total é: {}".format(latas*80))