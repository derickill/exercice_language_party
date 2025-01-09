let tableau = [23, 5, 12, 8, 19, 1, 35, 7, 14];

for (let i = 0; i < tableau.length - 1; i++) {
    for (let j = 0; j < tableau.length - 1 - i; j++) {
        if (tableau[j] > tableau[j + 1]) {
            let temp = tableau[j];
            tableau[j] = tableau[j + 1];
            tableau[j + 1] = temp;
        }
    }
}

console.log(tableau);
