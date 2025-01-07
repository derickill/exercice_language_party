class Plat:
    def __init__(self, nom, prix, temps_preparation):
        self.nom = nom
        self.prix = prix
        self.temps_preparation = temps_preparation

    def afficher_details(self):
        print(f"Plat: {self.nom}, Prix: {self.prix}€, Temps de préparation: {self.temps_preparation} minutes")

class Serveur:
    def __init__(self, nom):
        self.nom = nom
        self.commandes_prises = []

    def prendre_commande(self, plat):
        self.commandes_prises.append(plat)
class Restaurant:
    def __init__(self):
        self.plats_disponibles = []
        self.serveurs = []

    def ajouter_plat(self, plat):
        self.plats_disponibles.append(plat)

    def ajouter_serveur(self, serveur):
        self.serveurs.append(serveur)

    def afficher_menu(self):
        print("Menu du restaurant :")
        for plat in self.plats_disponibles:
            plat.afficher_details()

    def gerer_commandes(self):
        for serveur in self.serveurs:
            print(f"\nServeur: {serveur.nom}")
            for plat in serveur.commandes_prises:
                print(f"  Commande prise: {plat.nom}")


plat1 = Plat("Pizza Margherita", 12, 15)
plat2 = Plat("Burger", 8, 10)
plat3 = Plat("Salade César", 7, 5)
serveur1 = Serveur("Pierre")
serveur2 = Serveur("Marie")
restaurant = Restaurant()
restaurant.ajouter_plat(plat1)
restaurant.ajouter_plat(plat2)
restaurant.ajouter_plat(plat3)
restaurant.ajouter_serveur(serveur1)
restaurant.ajouter_serveur(serveur2)

restaurant.afficher_menu()
serveur1.prendre_commande(plat1)
serveur1.prendre_commande(plat2)
serveur2.prendre_commande(plat3)

restaurant.gerer_commandes()