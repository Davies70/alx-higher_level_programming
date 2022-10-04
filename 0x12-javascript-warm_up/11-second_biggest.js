#!/usr/bin/node

/* checks the biggest number */

const arg = process.argv;
const array = [];

if (arg.length === 2 || arg.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < arg.length; i++) {
    array.push(arg[i]);
  }
  array.sort((a, b) => b - a);
  console.log(array[1]);
}
