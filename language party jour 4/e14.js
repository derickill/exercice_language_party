let etudiants = [
    { nom: "derick", age: 20, note: 16 },
    { nom: "calixte", age: 22, note: 14 },
    { nom: "elyas", age: 19, note: 18 },
    { nom: "David", age: 21, note: 12 },
    { nom: "lyes", age: 23, note: 17 }
];

let meilleurEtudiant = etudiants[0];

for (let i = 1; i < etudiants.length; i++) {
    if (etudiants[i].note > meilleurEtudiant.note) {
        meilleurEtudiant = etudiants[i];
    }
}

console.log(meilleurEtudiant.nom);

for (let i = 0; i < etudiants.length; i++) {
    if (etudiants[i].note >= 15) {
        console.log(etudiants[i].nom);
    }
}

let somme = 0;

for (let i = 0; i < etudiants.length; i++) {
    somme += etudiants[i].note;
}

let moyenne = somme / etudiants.length;

console.log(moyenne);
