#!/usr/bin/node
const args = process.argv.slice(2);

const firstArgument = args[0] || 'No argument';
console.log(firstArgument);
