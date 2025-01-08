produit = c("Pomme", "Orange", "Banane", "Raisin")
quantite = c(50, 30, 20, 15)
prix = c(1.2, 0.8, 0.5, 2.0)
ventes = data.frame(Produit = produit, Quantite = quantite, Prix = prix)
ventes
ventes["Total"] = ventes$Quantite*ventes$Prix
ventes["Total"]