#!/usr/bin/node

const id = process.argv[2];
const endpoint = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');
request(endpoint, { json: true }, function (error, response, body) {
  if (error) throw error;
  const res = body.characters;
  for (const character of res) {
    request(character, { json: true }, function (error, response, body) {
      if (error) throw error;
      const res2 = body.name;
      console.log(res2);
    });
  }
});
