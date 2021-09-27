#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares
print("Informe 10 números: ")
par = 0
impar =0

for i in range(10):
    numero = float(input("Digite um número: "))
    if numero % 2 == 0:
        par +=1
    else:
        impar += 1
    
print("Números pares são: {:.2f}".format(par))
print("Números impar são: {:.2f}".format(impar))
