#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Get the URL and file path from command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a request to the provided URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Write the response body to the specified file
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
