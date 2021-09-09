#Faça um Programa que peça dois números e imprima o maior deles.

nmr1 = float(input("Digite um número:"))
nmr2 = float(input("Digite outro número:"))
nmr3 = float(input("Digite outro número:"))

if nmr1 > nmr2 and nmr1 > nmr3 :
    print("O maior número é: {}".format(nmr1))
elif nmr2 > nmr1 and nmr2 > nmr3 :
    print("O maior número é: {}".format(nmr2))
else:
    print("O maior número é: {}".format (nmr3))