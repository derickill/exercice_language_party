lancer = c(1,2,3,4,5,6)
result_apres_100 = sample(lancer, 100, replace = TRUE)
result_apres_100
frequence = table(result_apres_100)
frequence
barplot(frequence)
