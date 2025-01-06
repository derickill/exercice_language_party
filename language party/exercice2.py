# programme calculatrice
operation = input("que voulez vous faire? entrer +, -, / ou X")
if operation == "+":
    print("vous voulez faire une adition ")
    nbr1 = int(input("entrer ici le premier nombre"))
    nbr2 = int(input("entrer ici le deuxieme nombre"))
    resultat = nbr1 + nbr2
    print(f"le resultat est {resultat}")

if operation == "-":
    print("vous voulez faire une soustraction")
    nbr1 = int(input("entrer ici le premier nombre"))
    nbr2 = int(input("entrer ici le deuxieme nombre"))
    resultat = nbr1 - nbr2
    print(f"le resultat est {resultat}")

if operation == "/":
    print("vous voulez faire une division ")
    nbr1 = int(input("entrer ici le premier nombre"))
    nbr2 = int(input("entrer ici le deuxieme nombre"))
    if nbr2 != 0:
        resultat = nbr1/nbr2
        print(f"le resultat est {resultat}")
    else:
        print("impossible de diviser par 0")

if operation == "X" or operation == "x":
    print("vous voulez faire une multiplication ")
    nbr1 = int(input("entrer ici le premier nombre"))
    nbr2 = int(input("entrer ici le deuxieme nombre"))
    resultat = nbr1 * nbr2
    print(f"le resultat est {resultat}")