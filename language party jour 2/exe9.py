class Article:
    def __init__(self, nom, prix, quantite_en_stock):
        self.nom = nom
        self.prix = prix
        self.quantite_en_stock = quantite_en_stock

    def retirer_stock(self, quantite):
        if self.quantite_en_stock >= quantite:
            self.quantite_en_stock -= quantite
            return True
        return False


class Commande:
    def __init__(self, client):
        self.client = client
        self.articles_commandes = []

    def ajouter_article(self, article, quantite):
        self.articles_commandes.append((article, quantite))

    def calculer_total(self):
        total = 0
        for article, quantite in self.articles_commandes:
            total += article.prix * quantite
        return total

article1 = Article("shirt", 20, 100)
article2 = Article("Casquette", 15, 50)

commande = Commande("Alice")
commande.ajouter_article(article1, 3)
commande.ajouter_article(article2, 2)

total = commande.calculer_total()
print(f"Montant total de la commande : {total}€")

for article, quantite in commande.articles_commandes:
    if article.retirer_stock(quantite):
        print(f"{article.nom} : {quantite} unités retirées du stock.")
    else:
        print(f"{article.nom} : Stock insuffisant pour {quantite} unités.")
