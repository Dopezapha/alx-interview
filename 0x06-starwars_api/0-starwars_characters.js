#!/usr/bin/node

const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  request(`${API_URL}/films/${movieId}/`, (err, response, body) => {
    if (err) {
      console.error(err);
      return;
    }
    if (response.statusCode !== 200) {
      console.error(`Error: Status code ${response.statusCode}`);
      return;
    }
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, characterResponse, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
            return;
          }
          if (characterResponse.statusCode !== 200) {
            reject(new Error(`Status code ${characterResponse.statusCode}`));
            return;
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));
    Promise.all(charactersName)
      .then(names => {
        console.log(names.join('\n'));
      })
      .catch(allErr => {
        console.error(allErr);
      });
  });
} else {
  console.error('Please provide a movie ID');
}
