let tableau = [15, 22, 8, 34, 56, 42, 67, 11, 90, 4];

let minimum = tableau[0];
let maximum = tableau[0];

for (let i = 1; i < tableau.length; i++) {
    if (tableau[i] < minimum) {
        minimum = tableau[i];
    }
    if (tableau[i] > maximum) {
        maximum = tableau[i];
    }
}

console.log("Nombre minimum : " + minimum);
console.log("Nombre maximum : " + maximum);
