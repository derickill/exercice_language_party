class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def emprunter(self):
        if self.disponible ==True:
            self.disponible = False
            return True
        else:
            return False

    def rendre(self):
        self.disponible = True


class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.livres_empruntes = []

    def emprunter_livre(self, livre):
        if livre.emprunter():
            self.livres_empruntes.append(livre)
            return True
        return False

    def rendre_livre(self, livre):
        if livre in self.livres_empruntes:
            livre.rendre()
            self.livres_empruntes.remove(livre)
            return True
        return False


class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_livres(self):
        for livre in self.livres:
            if livre.disponible:
                print(f"{livre.titre} par {livre.auteur} 'Disponible'")
            else:
                print(f"{livre.titre} par {livre.auteur} Indisponible")

    def gerer_emprunt(self, utilisateur, livre, action):
        if action == "emprunter":
            if utilisateur.emprunter_livre(livre):
                print(f"{utilisateur.nom} a emprunté {livre.titre}")
            else:
                print(f"{livre.titre} est déjà emprunté")
        elif action == "rendre":
            if utilisateur.rendre_livre(livre):
                print(f"{utilisateur.nom} a rendu {livre.titre}")
            else:
                print(f"{utilisateur.nom} n'a pas ce livre à rendre")

livre1 = Livre("livre1", "puff")
livre2 = Livre("livre2", "denzel")
utilisateur1 = Utilisateur("jean")
bibliotheque = Bibliotheque()
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)

bibliotheque.afficher_livres()

bibliotheque.gerer_emprunt(utilisateur1, livre1, "emprunter")
bibliotheque.afficher_livres()

bibliotheque.gerer_emprunt(utilisateur1, livre1, "emprunter")  # Essayer de réemprunter le même livre

bibliotheque.gerer_emprunt(utilisateur1, livre1, "rendre")
bibliotheque.afficher_livres()