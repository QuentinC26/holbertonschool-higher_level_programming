#!/usr/bin/node
const process = require('process');
if (process.argv.length === 2) {
  console.log('0');
} else if (process.argv.length === 3) {
  console.log('0');
} else {
  args = process.argv.slice(2);
  const numbers = args.map(arg => Number(arg));
  numbers.sort((a, b) => a - b);
  console.log(numbers[numbers.length - 2]);
}
