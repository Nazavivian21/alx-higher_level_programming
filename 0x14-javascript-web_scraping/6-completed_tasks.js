#!/usr/bin/node

const request = require('request');

// API URL from the command line argument
const apiUrl = process.argv[2] || 'https://jsonplaceholder.typicode.com/todos';

// Make a request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response
  const todos = JSON.parse(body);
  const completedTasks = {};

  // Count completed tasks for each user
  todos.forEach(todo => {
    if (todo.completed) {
      const userId = todo.userId;
      if (!completedTasks[userId]) {
        completedTasks[userId] = 0;
      }
      completedTasks[userId]++;
    }
  });

  // Print the result
  console.log(completedTasks);
});
