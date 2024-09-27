#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];  // Get the API URL from the first argument
const wedgeAntillesId = '18';  // Wedge Antilles character ID

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
    if (error) {
        console.error('Error:', error);  // Print the error if one occurred
    } else {
        const films = JSON.parse(body).results;  // Parse the API response and get the films
        let count = 0;

        // Loop through each film and check if Wedge Antilles (ID 18) is in the character list
        films.forEach(film => {
            if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
                count++;
            }
        });

        // Print the number of movies where Wedge Antilles is present
        console.log(count);
    }
});
