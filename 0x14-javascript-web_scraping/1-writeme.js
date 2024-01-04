#!/usr/bin/node

const fileSystem = require('fs');

const targetFile = process.argv[2];
const fileContent = process.argv[3];

fileSystem.writeFile(targetFile, fileContent, 'utf-8', function (error) {
  if (error) {
    console.log(error);
  }
});
