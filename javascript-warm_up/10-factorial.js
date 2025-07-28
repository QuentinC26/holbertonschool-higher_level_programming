#!/usr/bin/node
function fact(number) {
    if (number === 0 || number === 1) {
        return 1;
    } else if (isNaN(Number(process.argv[2]))) {
        return 1;
    }
    return number * fact(number - 1);
}
console.log(fact(Number(process.argv[2])));