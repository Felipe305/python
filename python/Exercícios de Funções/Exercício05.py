#Faça um programa com uma função chamada somaImposto.
#A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
#A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    custo = custo + (custo * taxaImposto / 100.0)
    return custo


taxa = float(input("Informe o valor da taxa de imposto: "))
custo = float(input("Informe o valor de custo do produto: "))

custo = somaImposto(taxa,custo)

print("O preço com com impostos é %.2f" % custo)
