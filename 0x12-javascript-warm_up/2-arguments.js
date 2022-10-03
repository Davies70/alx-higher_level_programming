#!/usr/bin/node

/* process arguments */

const arg = process.argv;

if (arg.length === 2) {
  console.log('No argument');
}

if (arg.length === 3) {
  console.log('Argument found');
}

if (arg.length > 3) {
  console.log('Arguments found');
}
