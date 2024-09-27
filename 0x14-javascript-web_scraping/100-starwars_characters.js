#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line argument
const movieId = process.argv[2];

// Define the API URL with the movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a GET request to the API to fetch the movie details
request(apiUrl, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
        return;
    }

    // Parse the response body as JSON
    const movie = JSON.parse(body);
    
    // Loop through each character URL and make a request to fetch character details
    movie.characters.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
            if (charError) {
                console.error('Error:', charError);
                return;
            }

            // Parse the character data and print the character name
            const character = JSON.parse(charBody);
            console.log(character.name);
        });
    });
});
