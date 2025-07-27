#!/usr/bin/node
function add(a, b) {
  const process = require('process');
  a = Number(process.argv[3]);
  b = Number(process.argv[4]);
  return a + b;
}

if (isNaN(Number(process.argv[2]))) {
  console.log('NaN');
} else if(process.argv.length === 2) {
  console.log('NaN');
} else if(process.argv.length === 3) {
  console.log('NaN');
} else {
  const result = add();
  console.log(result)
}
