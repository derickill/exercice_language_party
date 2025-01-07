from select import select


class produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
    def afficher_produit(self):
        print(f"votre produit est {self.nom}.Son prix est {self.prix} et sa quantite est {self.quantite}")

class magazin(produit):
    list_prodiut = [produit("nutela",100,2),produit("beure", 105 ,5),produit("milk", 500,50)]
    def ajouter_produit(self,nouv_produit):
        self.list_prodiut.append(nouv_produit)
    def rechercher_produit(self, nomm):
        for recherche in self.list_prodiut:
            if recherche.nom == nomm:
                recherche.afficher_produit()
            else:
                print("le mot n'a pas ete trouver. Vous pouvez l'ajouter")
    def afficher_inventaire(self):
        for i in self.list_prodiut:
            print(i.afficher_produit())
    #def vendre_produit(self,vendre):






