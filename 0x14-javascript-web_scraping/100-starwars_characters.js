#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    return;
  }

  const movieData = JSON.parse(body);
  const charactersUrls = movieData.characters;

  // Function to retrieve character names from their URLs
  const getCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        }
      });
    });
  };

  // Iterate through character URLs and fetch character names
  Promise.all(charactersUrls.map(url => getCharacterName(url)))
    .then(characterNames => {
      characterNames.forEach(name => console.log(name));
    })
    .catch(err => {
      console.error(err);
    });
});
