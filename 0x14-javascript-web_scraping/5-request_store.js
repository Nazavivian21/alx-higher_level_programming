#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2]; // Get the URL from the first argument
const filePath = process.argv[3]; // Get the file path from the second argument

// Make a GET request to the provided URL
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error); // Print the error if one occurred
  } else {
    // Write the response body to the specified file in UTF-8 encoding
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error('Error writing to file:', err); // Print error if unable to write
      } else {
        console.log('File written successfully!');
      }
    });
  }
});
