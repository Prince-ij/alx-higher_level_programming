#!/usr/bin/node
const fs = require('fs');

const fF = process.argv[2];
const sF = process.argv[3];
const lF = process.argv[4];
const f = fs.readFileSync(fF.tostring());
const r = fs.readFileSync(sF.toString());
fs.writeFileSync(lF, f + r);
