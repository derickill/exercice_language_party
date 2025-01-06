# table de multiplication
print("vous voulez la table de multiplication d'un nombre ?")
nombre = int(input("entrer le nombre dont vous voulez la table de multiplication"))
print("la table de multiplication est donc")
a = 0
while a<=10:
    print(f"{nombre}X{a} = {nombre*a}")
    a += 1