nom = c("Alice", "Bob", "Clara")
note1 = c(15, 10, 12)
note2 = c(17, 14, 9)
notess = data.frame(Nom = nom, Note1 = note1, Note2= note2)
notess["moyenne1"] = (notess$Note1+notess$Note2)/2
notess
notess["moyenne2"] = apply(notess[c("Note1","Note2")], 1, mean)
notess