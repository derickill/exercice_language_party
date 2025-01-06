nbrr = int(input("entrer votre nombre ici"))
a = nbrr-1
if nbrr ==0:
    print("le resultat est 1")
else:
    while a!=0:
        nbrr = nbrr*a
        a -= 1
    print(f"le resultat est {nbrr}")
