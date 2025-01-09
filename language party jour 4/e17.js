fetch('https://official-joke-api.appspot.com/random_joke')
    .then(response => response.json())
    .then(data => {
        console.log("Setup : " + data.setup);
        console.log("Punchline : " + data.punchline);
    })
    .catch(error => console.log('Erreur:', error));
