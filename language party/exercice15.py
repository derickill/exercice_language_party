#jeu de devinette
import random as rd

nbr = rd.randint(0, 100)  # Générer un nombre aléatoire entre 0 et 100
print("Bienvenue au jeu de devinettes ! Vous avez 10 essais pour trouver le nombre.")

a = 0  # Compteur d'essais
while a < 10:  # Boucle externe pour gérer le nombre d'essais
    devine = int(input("À vous de jouer ! Devinez le nombre : "))

    while devine != nbr:  # Boucle interne pour guider le joueur
        if devine > nbr:
            print("Non, c'est moins !")
        elif devine < nbr:
            print("Non, c'est plus !")

        a += 1  # Incrémenter le compteur d'essais
        if a >= 10:  # Vérifier si le joueur a dépassé le nombre d'essais
            print(f"Dommage, vous avez perdu ! Le nombre était {nbr}.")
            break  # Sortir de la boucle interne

        devine = int(input("Essayez encore : "))  # Demander une nouvelle entrée

    if devine == nbr:  # Si le joueur a trouvé le bon nombre
        print(f"Félicitations ! Vous avez trouvé le nombre {nbr} en {a + 1} essais.")
        break  # Sortir de la boucle externe

# Si le joueur n'a pas gagné après 10 essais
if a >= 10 and devine != nbr:
    print(f"Dommage, vous avez perdu ! Le nombre était {nbr}.")
