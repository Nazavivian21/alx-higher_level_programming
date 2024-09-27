#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command line argument
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to the Star Wars API to get the movie details
request(apiUrl, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
        return;
    }
    
    const movie = JSON.parse(body);  // Parse the response to JSON
    const characters = movie.characters;  // Get the list of character URLs
    
    // Loop through each character URL and make a request to get the character's name
    characters.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
            if (charError) {
                console.error('Error:', charError);
                return;
            }
            const character = JSON.parse(charBody);
            console.log(character.name);  // Print each character's name
        });
    });
});
