#!/usr/bin/node
const num = process.argv[2];
const numInt = parseInt(num);
if (isNaN(numInt)) {
  console.log('Missing number of occurrences');
}
let i = 0;
while (i < numInt) {
  console.log('C is fun');
  ++i;
}
