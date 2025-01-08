library(dplyr)
nomm = c("alice", "bob", "clara", "david")
departement = c("RH", "IT", "IT", "Finance")
salaire = c(3000, 4500, 5000, 4000)
employes = data.frame(Nom = nomm, Salaire = salaire, Departement = departement)
employes

empl_IT = employes %>% filter(Departement == "IT") 
empl_IT

moyenne_salair = employes %>% group_by(Departement) %>% summarise(moyenne_par_dep=mean(Salaire))
moyenne_salair

croissant = employes %>% arrange(desc(Salaire))
croissant