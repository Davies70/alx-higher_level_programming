#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }

  fs.writeFile(process.argv[3], body, 'utf-8', function (error) {
    if (error) {
      return console.error(error);
    }
  });
});
