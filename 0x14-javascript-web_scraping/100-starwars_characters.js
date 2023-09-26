#!/usr/bin/node

const request = require('request');


const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;


request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  
  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
        
    movieData.characters.forEach((characterUrl) => {
      request.get(characterUrl, (charError, charResponse, charBody) => {
        if (!charError && charResponse.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  } else {
    console.error(`Failed to retrieve movie data. Status code: ${response.statusCode}`);
    process.exit(1);
  }
});
