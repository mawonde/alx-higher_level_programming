#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode === 200) {
    const filmsData = JSON.parse(body).results;
    const wedgeAntilles = filmsData.filter((film) => {
      return film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
    });

    console.log(wedgeAntilles.length);
  } else {
    console.error(`Failed to retrieve films data. Status code: ${response.statusCode}`);
    process.exit(1);
  }
});
