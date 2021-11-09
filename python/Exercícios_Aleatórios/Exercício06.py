
largura  = float(input("Digite quantos metros tem a largura da parede: "))
altura = float(input("Digite quantos metros de altura tem a parede: "))
area = largura*altura
tinta = area/2
print("Sua parede tem a dimensão de {}X{} e sua área é de {}m².\nPara pintar essa parede você precisara de {}".format(altura,largura,area,tinta))
