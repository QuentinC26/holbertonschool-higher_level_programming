#!/usr/bin/node
function add(a, b) {
  return a + b;
}

const process = require('process');
if (process.argv.length !== 4) {
  console.log('NaN');
} else {
  let a = Number(process.argv[2])
  let b = Number(process.argv[3])
  const result = add(a, b);
  console.log(result)
}
