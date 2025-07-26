#!/usr/bin/node
const process = require('process');

process.argv.forEach((argument, index) => {
    if (index === 1) {
        console.log("No argument")
    } else if (index === 2) {
        console.log(argument)
    }
});