#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a request to the Star Wars API to get movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body to JSON
  const data = JSON.parse(body);
  const characters = data.characters;

  // Use a loop to request each character and maintain the order
  printCharactersInOrder(characters, 0);
});

// Function to print each character in order
function printCharactersInOrder(characters, index) {
  if (index >= characters.length) {
    return; // Stop when all characters are printed
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    // Parse character data and print the name
    const characterData = JSON.parse(body);
    console.log(characterData.name);

    // Recursive call to get the next character in the list
    printCharactersInOrder(characters, index + 1);
  });
}
