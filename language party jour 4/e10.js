let tableau = [];
let somme = 0;
let max = 0;
let min = 100;
let countPair = 0;

for (let i = 0; i < 50; i++) {
    let nombre = Math.floor(Math.random() * 100) + 1;
    tableau.push(nombre);

    somme += nombre;
    if (nombre > max) max = nombre;
    if (nombre < min) min = nombre;
    if (nombre % 2 === 0) countPair++;
}

let moyenne = somme / tableau.length;
console.log(tableau)
console.log("Moyenne : " + moyenne);
console.log("Nombre le plus grand : " + max);
console.log("Nombre le plus petit : " + min);
console.log("Nombre de pairs : " + countPair);
