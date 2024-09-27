#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2]; // Get the API URL from the first argument

// Make a GET request to the provided API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error); // Print error if one occurred
  } else {
    const todos = JSON.parse(body); // Parse the response as JSON
    const completedTasks = {}; // Object to store completed task count for each user

    // Loop through each task and count completed ones by user
    todos.forEach(todo => {
      if (todo.completed) { // Only consider completed tasks
        if (completedTasks[todo.userId]) {
          completedTasks[todo.userId]++; // Increment the count for the user
        } else {
          completedTasks[todo.userId] = 1; // Initialize count for new user
        }
      }
    });

    // Print the user IDs and their corresponding task counts
    for (const userId in completedTasks) {
      console.log(`User ${userId}: ${completedTasks[userId]}`);
    }
  }
});
