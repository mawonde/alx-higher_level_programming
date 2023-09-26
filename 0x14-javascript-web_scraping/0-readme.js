#!/usr/bin/node

const fs = require('fs');

// Check if the file path is provided as an argument
if (process.argv.length < 3) {
  console.error('Usage: node read-file.js <file-path>');
  process.exit(1);
}

const filePath = process.argv[2];

// Read the file asynchronously in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
