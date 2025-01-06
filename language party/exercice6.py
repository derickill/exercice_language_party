#jeu de devinette
import random as rd
nbr = rd.randint(1,100)
devine = int(input("à vous de jouer"))
while devine != nbr:
    if devine>nbr:
        print("non c'est moins ")
    elif devine<nbr:
        print("non c'est plus")
    devine = int(input("encore"))
print("vous avez gagnez")
