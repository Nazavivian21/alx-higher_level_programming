#!/usr/bin/node
const args = process.argv.slice(2);

const x = parseInt(args[0], 10);

for (let i = 0; i < x || isNaN(x); i++) {
  if (isNaN(x)) {
    console.log('Missing number of occurrences');
    break;
  } else {
    console.log('C is fun');
  }
}
