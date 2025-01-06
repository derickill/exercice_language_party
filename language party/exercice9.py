mot = input("entrer un mot ici")
Liste = list(mot)
Liste.reverse()
new=""
for a in Liste:
    new +=a
if new == mot:
    print("votre mot est un palindrom")
else:
    print("non desole")
