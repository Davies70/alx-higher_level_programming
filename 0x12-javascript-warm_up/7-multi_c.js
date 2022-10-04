#!/usr/bin/node

/* prints according to command line argument */

const arg = process.argv;

if (!arg[2] || Object.is(NaN, Number(arg[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(arg[2]); i++) {
    console.log('C is fun');
  }
}
