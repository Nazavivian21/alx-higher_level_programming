#!/usr/bin/node

const request = require('request');

// API URL for Star Wars films
const apiUrl = process.argv[2] || 'https://swapi-api.alx-tools.com/api/films/';

// Character ID for Wedge Antilles
const wedgeAntillesID = 18;

// Make a request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response
  const films = JSON.parse(body);
  let count = 0;

  // Count the number of films that include Wedge Antilles
  films.results.forEach(film => {
    if (film.characters) {
      film.characters.forEach(character => {
        if (character.includes(`/${wedgeAntillesID}/`)) {
          count++;
        }
      });
    }
  });

  // Print the result
  console.log(count);
});
