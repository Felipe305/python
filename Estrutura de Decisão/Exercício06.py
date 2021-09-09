
#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.


vogais = ["A","E","I","O","U"]

for i in range(5):
    letra = input("Digite uma letra:").upper()

    achou = 0

    for i in vogais:
        if letra == i:
            achou = 1
            break
    if achou > 0:
        print("Vogal")
    else:
        print("Consoante")
    
    
    




     