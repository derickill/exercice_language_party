# compter le nombre de voyelle
phrase = input("entrer un phrase ici")
lettre = list(phrase)
a = 0
for x in lettre:
    if x in ['a', 'e', 'i', 'o', 'u', 'y']:
        a +=1
print(f"vous avez {a} voyelles dans votre phrase")