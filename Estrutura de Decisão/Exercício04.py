#descubra se um número é primo 

a = int(input("Digite um número:"))
div = 0

for i in range(1, a+1):
    resto = a
    if resto == 0:
        div = div + 1


if div == 2:
    print(f"número {a} é primo")
else:
    print(f"número {a} não é primo")
