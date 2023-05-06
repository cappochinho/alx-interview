#!/usr/bin/node

const id = process.argv[2];
const endpoint = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');
request(endpoint, function (error, response, body) {
  if (error) throw error;
  const res = JSON.parse(body).characters;
  for (const character of res) {
    request(character, function (error, response, body) {
      if (error) throw error;
      const res2 = JSON.parse(body).name;
      console.log(res2);
    });
  }
});
