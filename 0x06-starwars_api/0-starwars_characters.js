#!/usr/bin/node

const id = process.argv[2];
const endpoint = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');
request(endpoint, { json: true }, function (error, response, body) {
  if (error) throw error;
  const res = body.characters;
  const names = [];
  for (const character of res) {
    names.push(new Promise((resolve, reject) => {
      request(character, { json: true }, function (error, response, body) {
        if (error) reject(error);
        resolve(body.name);
      });
    }));
  }
  Promise.all(names).then(name => {
    for (const person of name) {
      console.log(person);
    }
  }).catch(error => {
    console.error(error);
  });
});
