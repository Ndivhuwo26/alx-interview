#!/usr/bin/node

/* star wars api */

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;


request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  
  const film = JSON.parse(body);
  const characters = film.characters;

  
  const printCharacterNames = (index) => {
    if (index >= characters.length) return;

   
    request(characters[index], (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

     
      const character = JSON.parse(body);
      console.log(character.name);

      
      printCharacterNames(index + 1);
    });
  };

  
  printCharacterNames(0);
});

