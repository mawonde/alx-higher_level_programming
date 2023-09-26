#!/usr/bin/node

const fs = require('fs');
const request = require('request');


const url = process.argv[2];
const filePath = process.argv[3];


request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error('Error writing to file:', err);
        process.exit(1);
      } else {
        console.log(`Successfully saved the webpage content to ${filePath}`);
      }
    });
  } else {
    console.error(`Failed to retrieve webpage content. Status code: ${response.statusCode}`);
    process.exit(1);
  }
});
