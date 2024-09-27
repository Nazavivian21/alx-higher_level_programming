#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];  // Get the file path from the first argument


fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
        // If an error occurred, print the error object
        console.error(err);
    } else {
        // Print the file content
        console.log(data);
    }
});
