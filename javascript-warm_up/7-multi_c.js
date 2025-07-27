#!/usr/bin/node
const process = require('process');
const sentence = 'C is fun';
for (let index = 0; index < Number(process.argv[2]); index++) {
  console.log(sentence);
}
