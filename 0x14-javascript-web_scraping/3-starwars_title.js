#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2]; // Get the movie ID from the first argument
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`; // Construct the API URL

// Make a GET request to the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error); // Print the error if one occurred
  } else {
    // Parse the JSON response body
    const movie = JSON.parse(body);
    // Print the title of the movie
    console.log(movie.title);
  }
});
