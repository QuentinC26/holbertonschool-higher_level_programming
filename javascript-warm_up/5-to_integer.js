#!/usr/bin/node
const process = require('process');

if (process.argv.length === 2) {
  console.log('Not a number');
} else if (process.argv.length === 3) {
  if (Number(process.argv[2])) {
    console.log('My Number: %d', process.argv[2]);
  } else if (parseFloat(process.argv[2])) {
      console.log('My Number: %d', parseInt(process.argv[2]));
  } else if (isNaN(Number(process.argv[2]))) {
    console.log("Not a number");
  } 
}
