class voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
    def afficher_details(self):
        details = print(f"votre voiture de la marque {self.marque} et de modele {self.modele} a ete conçu en {self.annee} et a un kilometrage de {self.kilometrage} km/h")
        return details
    def augmenter_kilometrage(self,ajout):
        if self.kilometrage + ajout>self.kilometrage:
            self.kilometrage +=ajout
            print(f"le kilometrage est maintenant de {self.kilometrage} km/h")
            print(f"on a donc  {self.marque}  de modele {self.modele} conçu en {self.annee} et  kilometrage de {self.kilometrage} km/h")
        else:
            print("non impossible,le kilomztrage ne peut pas diminuer")

voiture1 = voiture("mercedes", "GLE", 2019, 400)
voiture1.afficher_details()
voiture1.augmenter_kilometrage(1000)
print("une autre voiture maintenant")
voiture2 = voiture("tesla", "modele Y", "2022", 300)
voiture2.afficher_details()
voiture2.augmenter_kilometrage(-10)
