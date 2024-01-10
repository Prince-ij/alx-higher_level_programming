#!/usr/bin/node
const fs = require('fs');

const fF = process.argv[2];
const sF = process.argv[3];
const lF = process.argv[4];
const f = fs.readFile(fF.tostring());
const r = fs.readFile(sF.toString());
fs.writeFile(f + r);
