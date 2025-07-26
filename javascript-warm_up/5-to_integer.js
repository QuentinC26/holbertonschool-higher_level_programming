#!/usr/bin/node
const process = require('process');

if (process.argv.length === 2) {
  console.log('Not a number');
} else if (process.argv.length === 3) {
  if (Number(process.argv[2])) {
    console.log('My number: %d', Math.floor(process.argv[2]));
  } else if (isNaN(Number(process.argv[2]))) {
    console.log("Not a number");
  }
}
