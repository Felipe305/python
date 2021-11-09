#Conversor de moeda:

moeda = float(input("Digite um valor em reais:"))

dolar = moeda/5.37

print("Com R${} você pode comprar ${:.2f}".format(moeda,dolar))