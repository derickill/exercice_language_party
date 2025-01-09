import fetch from 'node-fetch'

const nouveauPost = {
    title: 'Mon premier post',
    body: 'Ceci est le contenu de mon post.',
    userId: 1
};

fetch('https://jsonplaceholder.typicode.com/posts', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(nouveauPost)
})
    .then(response => response.json())
    .then(postCree => {
        console.log('Post créé :', postCree);


        return fetch('https://jsonplaceholder.typicode.com/posts?_limit=10');
    })
    .then(response => response.json())
    .then(posts => {
        console.log('Les 10 premiers posts :');
        posts.forEach(post => {
            console.log(`ID: ${post.id}, Titre: ${post.title}`);
        });
    })
    .catch(error => console.log('Erreur:', error));
