const serie = "10, 20, 30, 40";
let nombre = serie.split(",");
nombre = nombre.map(Number);
console.log(nombre);
let nombreElements = nombre.length;
console.log("le nombre d'elements est ",nombreElements);
let somme = nombre.reduce((acc, valeur) => acc + valeur, 0);
console.log("la somme est ",somme);
let moyenne = somme / nombreElements;
console.log("la moyenne est ",moyenne);
let supMoyenne = 0;
for (let i = 0; i < nombreElements; i++) {
    if (nombre[i] > moyenne) {
        supMoyenne++;
    }
}
console.log("le nombre de nombre supperieur à la moyenne est ",supMoyenne)
