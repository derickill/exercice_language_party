let votes = ["Pomme", "Banane", "Orange", "Pomme", "Raisin", "Banane", "Banane"];

let resultat = {};

for (let i = 0; i < votes.length; i++) {
    let fruit = votes[i];
    if (resultat[fruit]) {
        resultat[fruit]++;
    } else {
        resultat[fruit] = 1;
    }
}

console.log(resultat);

let gagnant = "";
let maxvote = 0;

for (let fruit in resultat) {
    if (resultat[fruit] > maxvote) {
        gagnant = fruit;
        maxvote = resultat[fruit];
    }
}

console.log("Le fruit gagnant est : " + gagnant);
