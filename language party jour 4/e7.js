let tableau = [10, 20, 30, 40, 50];

if (tableau.length === 0) {
    console.log("Le tableau est vide");
} else {
    let somme = 0;
    for (let i = 0; i < tableau.length; i++) {
        somme += tableau[i];
    }
    let moyenne = somme / tableau.length;
    console.log("La moyenne est : " + moyenne);
}
