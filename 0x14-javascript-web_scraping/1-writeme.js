#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2]; // Get the file path from the first argument
const stringToWrite = process.argv[3]; // Get the string to write from the second argument

// Write the string to the file in utf-8
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    // If an error occurred, print the error object
    console.error(err);
  } else {
    // If no error, print a success message
    console.log('File has been written successfully!');
  }
});
