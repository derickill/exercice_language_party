#moyenne note
note = (input("entrer toute vos notes separer par une vigule"))
ouais = note.split(sep=",")
n = 0
for a in ouais:
    n += int(a)
fin = n/len(ouais)
print(f"la moyenne est {fin}")
