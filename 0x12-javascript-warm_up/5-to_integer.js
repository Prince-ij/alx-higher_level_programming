#!/usr/bin/node
const num = process.argv[2];
const numInt = parseInt(num);
if (!isNaN(numInt)) {
  console.log(`My number: ${numInt}`);
} else {
  console.log('Not a number');
}
