import random
wyniky = 0
wynikx = 0
while wynikx<3 and wyniky<3:
    print ("1 - Papier, 2 - Kamień, 3 - Nożyce")

    print("Twój ruch: ") 
    x = input()
    x = int(x)

    y = random.randint(1,3)
    if y == 1:
        print("Przeciwnik wybiera : Papier")
    elif y == 2:
        print("Przeciwnik wybiera : Kamień")
    else:
        print("Przeciwnik wybiera : Nożyce")



    if x == 1 and y == 2 or x == 2 and y == 3 or x == 3 and y == 1:
        print("Wygrana!!!") 
        wynikx +=1
    elif x == 1 and y == 3 or x == 2 and y == 1 or x == 3 and y == 2:
        print("Przegrana :)")
        wyniky +=1
    else:
        print("Powtórz")
    print("Ty : ", wynikx)
    print("Komputer : ", wyniky)   
if wynikx == 3:
    print("gratulacje jesteś lepszy od twojego kompa wyrzuć go :)")
else:
    print ("jesteś słaby")