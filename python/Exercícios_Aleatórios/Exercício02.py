#Crie um algoritmo que mostre o dobro, triplo e raiz quadrada!

n = int(input("Digite um número: "))

d = n * 2
t = n * 3
r = n ** 2

print("O dobro de {} é {} \nE o triplo de {} é {} \nE raiz quadrada de {} é {:.2f} ".format(n,d,n,t,n,r))