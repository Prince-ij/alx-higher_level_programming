#!/usr/bin/node
const num = process.argv[2];
const numInt = parseInt(num);
if (isNaN(numInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: "${numInt}"`);
}
