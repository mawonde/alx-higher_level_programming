#!/usr/bin/node

const request = require('request');


const apiUrl = process.argv[2];


request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  
  if (response.statusCode === 200) {
    const tasksData = JSON.parse(body);

 
    const tasksDone = tasksData.filter((task) => task.completed);

   
    const tasksDoneCount = new Map();

    for (const task of tasksDone) {
      if (tasksDoneCount.has(task.userId)) {
        tasksDoneCount.set(task.userId, tasksDoneCount.get(task.userId) + 1);
      } else {
        tasksDoneCount.set(task.userId, 1);
      }
    }

    
    tasksDoneCount.forEach((count, userId) => {
      console.log(`'${userId}': ${count}`);
    });
  } else {
    console.error(`Failed to retrieve task data. Status code: ${response.statusCode}`);
    process.exit(1);
  }
});
