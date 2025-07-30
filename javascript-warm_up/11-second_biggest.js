#!/usr/bin/node
const process = require('process');
if (Number(process.argv.length) === 2) {
  console.log('0');
} else if (Number(process.argv.length) === 3) {
  console.log('0');
} else {
    biggest_second = []
    args = process.argv.slice(2)
    for (index = 0; index < args.length; index++) {
          biggest_second.push((args[index]))
          biggest_second.reverse();
        }
   console.log(biggest_second[1])
}
