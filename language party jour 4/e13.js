function calculer(nombre1, nombre2, operation) {
    if (operation === "+") {
        return nombre1 + nombre2;
    } else if (operation === "-") {
        return nombre1 - nombre2;
    } else if (operation === "*") {
        return nombre1 * nombre2;
    } else if (operation === "/") {
        if (nombre2 === 0) {
            return "Erreur : Division par zéro";
        } else {
            return nombre1 / nombre2;
        }
    } else {
        return "Opération non valide";
    }
}

let resultat = calculer(10, 5, "+");
console.log(resultat);
