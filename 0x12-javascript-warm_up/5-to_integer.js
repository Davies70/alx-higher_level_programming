#!/usr/bin/node

/* converts to integer*/

const args = process.argv;

if (Object.is(NaN, Number(args[2])) || !args[2]) {
  console.log('Not a number');
} else {
  console.log('My number: ' + args[2]);
}
