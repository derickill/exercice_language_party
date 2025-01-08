nom = c("alice", "bob", "clara", "david", "emma", "fred", "gina")
age = c(22, 25, 20, 23, 24, 26, 21)
note = c(15, 18, 4, 16, 17, 19, 20)
etudiant = data.frame(Nom=nom, Age=age, Note = note)
etudiant$Nom
etudiant$Note
etudiant[etudiant$Note>=15,]