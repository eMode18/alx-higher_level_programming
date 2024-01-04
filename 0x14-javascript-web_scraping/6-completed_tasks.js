#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    return;
  }
  const todos = JSON.parse(body);
  const completedTasks = {};
  todos.forEach((task) => {
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId]++;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  });
  console.log(completedTasks);
});
