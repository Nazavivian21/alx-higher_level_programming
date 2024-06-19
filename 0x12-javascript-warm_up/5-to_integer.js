#!/usr/bin/node
const args = process.argv.slice(2);

const arg1 = Number(args[0]);

if (Number.isInteger(arg1)) {
  console.log(`My number: ${arg1}`);
} else {
  console.log('Not a number');
}
