class animal:
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece
    def parler(self):
        return "je suis un animal"
class chien(animal):
    def parler(self):
        return "Wouf"

class chat(animal):
    def parler(self):
        return "Miaou"

class zoo():
    list_animaux = ["Chien","Chat","Lion","Tigre","Éléphant"]
    def afficher_list_animaux(self):
        return print(f"la liste des animaux est {self.list_animaux}")
    def ajouter_animal(self,animal):
        self.list_animaux.append(animal)

    def faire_parler_tout_le_monde(self):
        for i in self.list_animaux:
            print("je suis un animal")

