#!/usr/bin/node
const process = require('process');

if (process.argv.length === 2) {
  console.log('%s is %s', process.argv.length[0], process.argv.length[0]);
} else if (process.argv.length === 3) {
  console.log('%s is %s', process.argv.length[3], process.argv.length[0]);
} else {
  console.log('%s is %s', process.argv.length[3], process.argv.length[4]);
}
