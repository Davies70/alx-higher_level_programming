#!/usr/bin/node

/* factorial */

const arg = process.argv;

function factorial (n) {
  if (!n || n < 0 || Object.is(NaN, n)) {
    return (1);
  }
  if (n === 0) {
    return (1);
  }
  return (n * factorial(n - 1));
}

console.log(factorial(Number(arg[2])));
