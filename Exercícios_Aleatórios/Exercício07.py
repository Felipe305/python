#Descontos produtos

preço = float(input("Digite o valor do produto:"))
desconto = preço - (preço*5)/100


print("O valor do produto fica R${} com desconto de 5% ".format(desconto))