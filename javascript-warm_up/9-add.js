#!/usr/bin/node
const process = require('process');
function add(a, b) {
  if (process.argv.length < 4) {
    console.log('NaN');
  } else if (isNaN(Number(process.argv[4])))
    a = Number(process.argv[3]);
    b = Number(process.argv[4]);
    console.log(a + b);
}
