nob = input("Entrez vos nombres, séparés par une virgule")
liste_de_nombre = [float(i) for i in nob.split(sep=",")]

print(sorted(liste_de_nombre))
