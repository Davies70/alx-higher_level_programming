#!/usr/bin/node

const fs = require('fs');
const arg = process.argv;

const file1 = fs.readFileSync(arg[2], 'utf8');
const file2 = fs.readFileSync(arg[3], 'utf8');

fs.writeFileSync(arg[4], file1 + file2);
