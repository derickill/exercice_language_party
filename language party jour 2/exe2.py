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

    def calculer_age(self,annee_actu):
        age = annee_actu - self.annee
        return age

    def est_vieille(self, annee_actu):
        df = self.calculer_age(annee_actu)
        if df>10:
            return True
        else:
            return False

voi1 = voiture("alto", "x200", 2018, 180)
voi1.afficher_details()
print(f"l'age de la voiture est {voi1.calculer_age(2025)} ans")
print(f"la voiture est vielle ?: {voi1.est_vieille(2025)}")
print("une autre voiture maintenant")
voi2 = voiture("GMC", "1x", 2019, 200)
voi2.afficher_details()
print(f"l'age de la voiture est {voi2.calculer_age(2025)} ans")
print(f"la voiture est vielle ?: {voi2.est_vieille(2025)}")