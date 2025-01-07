class personne:
    def __init__(self, nom, point_de_vie, force):
        self.nom = nom
        self.point_de_vie= point_de_vie
        self.force = force
    def attaquer(self,autre_personnage):
        nom1 = self.nom
        nom2 = autre_personnage.nom
        force1 = self.force
        vie1 = self.point_de_vie
        force2 = autre_personnage.force
        vie2 = autre_personnage.point_de_vie
        while vie1 >=0 and vie2>=0:
            vie1 -=force2
            vie2 -= force1
        if vie1<=0:
            print(f"{nom2} a gagner")
        elif vie2<=0:
            print(f"{nom1} a gagner")


class guerrier(personne):
    def __init__(self,nom,point_de_vie, force):
        super().__init__(nom, point_de_vie, force)
        self.nom="Guerrier"
        self.force = 20+force

class mage(personne):
    def __init__(self, nom, point_de_vie, force):
        super().__init__(nom, point_de_vie, force)
        self.nom = "mage"
    def degat_sup(self,degat):
        self.force += degat


jeu = guerrier("gerrier", 500, 00)
magge = mage("mage", 500, 100)
jeu.attaquer(magge)