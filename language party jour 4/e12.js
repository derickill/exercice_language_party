let personne = {
    nom: "Alice",
    age: 30,
    adresse: {
        rue: "Rue epita",
        ville: "Paris",
        codePostal: "75000"
    },
    hobbies: ["Lecture", "Natation", "Voyages"]
};

console.log(personne);

personne.hobbies.push("Cinéma");

personne.age = 35;

delete personne.adresse.codePostal;

console.log(personne);
