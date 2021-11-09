##Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares

print("Informe 10 números")
print("-=-"* 20)

par = 0
impar = 0


for i in range(1,10):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    
print("Numeros pares são: {}".format(par))
print("Números impar são: {}".format(impar))
    