#Faça um Programa que leia três números e mostre-os em ordem decrescente

nmr1 = int(input("Digite um número:"))
nmr2 = int(input("Digite outro  número:"))
nmr3 = int(input("Digite o terceiro número:"))

if (nmr1 >= nmr2) and (nmr1 >= nmr3):
    print(nmr1)
    if (nmr2 >= nmr3):
        print(nmr2)
        print(nmr3)
    else:
        print(nmr3)
        print(nmr2)
elif nmr2 >= nmr1:
    print(nmr2)
    if (nmr1 >= nmr3):
        print(nmr1)
        print(nmr3)
    else:
        print(nmr3)
        print(nmr1)
else:
    print(nmr3)
    if (nmr1 >= nmr2):
        print(nmr1)
        print(nmr2)
    else:
        print(nmr2)
        print(nmr1)







