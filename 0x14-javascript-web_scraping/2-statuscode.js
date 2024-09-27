#!/usr/bin/node
const request = require('request');
const url = process.argv[2]; // Get the URL from the first argument

// Make a GET request to the provided URL
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error); // Print the error if one occurred
  } else {
    console.log(`code: ${response.statusCode}`); // Print the status code
  }
});
