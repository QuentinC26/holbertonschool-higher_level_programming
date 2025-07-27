#!/usr/bin/node
const process = require('process');
const caracters = 'X';
if (isNaN(Number(process.argv[2]))) {
  console.log("Missing size");
}
let index = 0;
for (let index = 0; index < Number(process.argv[2]); index++) {
  process.stdout.write(caracters);
}
console.log()
