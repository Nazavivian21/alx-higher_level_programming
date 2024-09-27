#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// Define the API endpoint with the movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to get the movie details
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Check if the request was successful (status code 200)
  if (response.statusCode === 200) {
    // Parse the response body to get the movie data
    const movie = JSON.parse(body);
    
    // Get the list of character URLs
    const characters = movie.characters;

    // For each character URL, make a request to get the character details
    characters.forEach(characterUrl => {
      request(characterUrl, function (charError, charResponse, charBody) {
        if (charError) {
          console.error('Error:', charError);
          return;
        }

        if (charResponse.statusCode === 200) {
          // Parse the character details and print the character's name
          const character = JSON.parse(charBody);
          console.log(character.name);
        }
      });
    });
  } else {
    console.error(`Failed to fetch movie. Status code: ${response.statusCode}`);
  }
});
