#!/usr/bin/node
const process = require('process');

if (process.argv.length === 2) {
  console.log('%s is %s', "undefined", "undefined");
} else if (process.argv.length === 3) {
  console.log('%s is %s', process.argv[2], "undefined");
} else if (process.argv.length === 4) {
  console.log('%s is %s', process.argv[2], process.argv[3]);
}
