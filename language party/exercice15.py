#jeu de devinette
import random as rd
nbr = rd.randint(1,1000)
devine = int(input("à vous de jouer"))
a = 0
while a<10:
    if devine == nbr:
        print("you win")
    if devine>nbr:
        print("c'est plus")
    elif devine<nbr:
        print("non c'est")
    a +=1
    devine = int(input("réessayez encore "))
print("nombre d'essai fini.Le jeu est terminé ")

