#moyenne note
note = (input("Entrez toutes vos notes, séparées par une virgule"))
ouais = note.split(sep=",")
n = 0
for a in ouais:
    n += int(a)
fin = n/len(ouais)
print(f"la moyenne est {fin}")
