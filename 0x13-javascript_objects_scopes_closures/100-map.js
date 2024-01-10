#!/usr/bin/node
list = require('./100-data.js').list;
newList = list.map((x, id) => x * id);
console.log(newList);
