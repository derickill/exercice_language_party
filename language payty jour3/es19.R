library("ggplot2")
mois = c("Janvier"," Février", "Mars", "Avril")
chiffreAffaires = c(1000, 1200, 1500, 1700)
ventes = data.frame(Mois = mois, ChiffreAffaires = chiffreAffaires)
ggplot(ventes, aes(x = Mois, y = ChiffreAffaires , group = 1)) +
  geom_line(arrow = arrow()) + geom_point() + ggtitle("Chiffre Affaires en fonction des mois ")