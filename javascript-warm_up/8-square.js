#!/usr/bin/node
const process = require('process');
const caracters = 'X';
if (isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
}
for (let index = 0; index < Number(process.argv[2]); index++) {
  for (let index2 = 0; index2 < Number(process.argv[2]); index2++) {
    process.stdout.write(caracters);
  }
  console.log();
}
