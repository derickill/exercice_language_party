class livre:
    #bibliotheque = {"Livre 1": True, "Livre 2": "disponible", "Livre 3": "indisponible", "Livre 4": "disponible"}
    def __init__(self, titre, auteur, disponible):
        self.titre = titre
        self.auteur = auteur
        self.disponible = disponible
    def emprunter(self,nom_livre):
        #if self.bibliotheque[nom_livre]==True:
            #self.bibliotheque[nom_livre]=False
        #elif:
        if self.disponible == True:
            self.disponible=False
            print("vous avez bien empruter le livre")
        else:
            print("le livre n'est pas disponible")
    def rendre(self,nom_livre):
        #if self.bibliotheque[nom_livre]==False:
          #  self.bibliotheque[nom_livre]=True
        #elif:
         #   print("le livre est deja disponible")
        if self.disponible == False:
            self.disponible=True
            print("vous avez bien rendu le livre")
        else:
            print("vous avez deja rendu le livre")

class utilisateur:
    def __init__(self, nom, livre_emprunte):
        self.nom = nom
        self.livre_emprunte = livre_emprunte
    def enprunter_livre(self,livre):
        self.livre_emprunte.append(livre)
        print(f"votre liste de livre enprunter est donc {self.livre_enprunte}")
    def rendre_livre(self,livre):
        if livre in self.livre_emprunte:
            del self.livre_emprunte[livre]
            print("vous avez rendu le livre")
            print(f"votre liste de livre est donc {self.livre_emprunte}")
        else:
            print("le livre n'a pas ete trouver")

class bibliotheque(livre):



