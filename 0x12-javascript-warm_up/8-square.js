#!/usr/bin/node

/* prints a square */

const arg = process.argv;
const array = [];

if (!arg[2] || Object.is(NaN, Number(arg[2]))) {
  console.log('Missing size');
}

for (let i = 0; i < Number(arg[2]); i++) {
  for (let j = 0; j < Number(arg[2]); j++) {
    array[j] = 'X';
  }
  console.log(array.join(''));
}
