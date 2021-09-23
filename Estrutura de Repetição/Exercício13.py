
print("Informe 10 números")
print("-=-"* 20)

par = 0
impar = 0

for i in range(1,11):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"Números pares: {par}")

print(f"Números impares: {impar}")
