#!/usr/bin/node
function add(a, b) {
  const process = require('process');
  a = Number(process.argv[3]);
  b = Number(process.argv[4]);
  return a + b;
}

if (process.argv.length !== 4) {
  console.log('NaN');
} else {
  const result = add();
  console.log(result)
}
