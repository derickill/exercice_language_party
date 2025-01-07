class Employe:
    def __init__(self, nom, salaire_base):
        self.nom = nom
        self.salaire_base = salaire_base

    def calculer_salaire(self):
        pass

class EmployeMensuel(Employe):
    def calculer_salaire(self):
        return self.salaire_base

class EmployeHoraire(Employe):
    def __init__(self, nom, salaire_base, heures_travaillees):
        super().__init__(nom, salaire_base)
        self.heures_travaillees = heures_travaillees

    def calculer_salaire(self):
        return self.salaire_base * self.heures_travaillees
class Entreprise:
    def __init__(self):
        self.employes = []

    def ajouter_employe(self, employe):
        self.employes.append(employe)

    def calculer_masse_salariale(self):
        total = 0
        for employe in self.employes:
            total += employe.calculer_salaire()
        return total
employe1 = EmployeMensuel("Alice", 2000)
employe2 = EmployeHoraire("Bob", 15, 160)
employe3 = EmployeMensuel("Charlie", 1800)
entreprise = Entreprise()
entreprise.ajouter_employe(employe1)
entreprise.ajouter_employe(employe2)
entreprise.ajouter_employe(employe3)
masse_salariale = entreprise.calculer_masse_salariale()
print(f"La masse salariale totale est : {masse_salariale}")
