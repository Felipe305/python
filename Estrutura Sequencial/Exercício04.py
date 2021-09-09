#Faça um Programa que peça as 4 notas bimestrais e mostre a média.#

notas01 = int(input("Digite uma nota:"))
notas02 = int(input("Digite uma nota:"))
notas03 = int(input("Digite uma nota:"))
notas04 = int(input("Digite uma nota:"))
media = (notas01+notas02+notas03+notas04)/4

if notas01 <= 10 and notas02 <= 10 and notas03 <= 10 and notas04 <= 10:
    print("A média é: {}".format(media))
else:
    print("Foi informado alguma nota errada")










