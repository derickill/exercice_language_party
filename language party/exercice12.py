import random as rd
lon = int(input("donner la longeur du mo de pass"))
caracteres = [chr(i) for i in range(32, 127)]
password = ""
for i in range(lon):
    nf = rd.randint(0,len(caracteres)-1)
    password += caracteres[nf]

print(password)

