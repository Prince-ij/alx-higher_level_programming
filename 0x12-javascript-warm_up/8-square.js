#!/usr/bin/node
const num = process.argv[2];
const numInt = parseInt(num);
if (isNaN(numInt)) {
  console.log('Missing size');
}
let square = '';
let i;
for (i = 0; i < numInt; ++i) square += 'x';
let j = 0;
while (j < numInt) {
  console.log(square);
  ++j;
}
