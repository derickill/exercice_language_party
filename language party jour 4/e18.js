import fetch from 'node-fetch'

let ville = "Paris";


fetch(`https://nominatim.openstreetmap.org/search?q=${ville}&format=json`)
    .then(response => response.json())
    .then(data => {
        if (data.length > 0) {
            let latitude = data[0].lat;
            let longitude = data[0].lon;


            fetch(`https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current_weather=true`)
                .then(response => response.json())
                .then(weatherData => {
                    let temperature = weatherData.current_weather.temperature;
                    let conditions = weatherData.current_weather.weathercode;


                    let conditionsText = "";
                    if (conditions === 0) conditionsText = "Clair";
                    else if (conditions === 1) conditionsText = "Légèrement nuageux";
                    else if (conditions === 2) conditionsText = "Nuageux";
                    else if (conditions === 3) conditionsText = "Pluie légère";
                    else if (conditions === 4) conditionsText = "Pluie modérée";
                    else if (conditions === 5) conditionsText = "Pluie forte";


                    console.log(`Température actuelle à ${ville}: ${temperature}°C`);
                    console.log(`Conditions météorologiques : ${conditionsText}`);
                })
                .catch(error => console.log('Erreur Open-Meteo:', error));
        } else {
            console.log('Ville non trouvée');
        }
    })
    .catch(error => console.log('Erreur Nominatim:', error));
