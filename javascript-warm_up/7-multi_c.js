#!/usr/bin/node
const process = require('process');
sentence = 'C is fun';
for (index = 0; index < Number(process.argv[2]); index++)
  console.log(sentence);
