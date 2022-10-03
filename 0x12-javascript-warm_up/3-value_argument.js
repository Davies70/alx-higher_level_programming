#!/usr/bin/node

/* prints the first argumeent passed */

const args = process.argv;

if (!args[2]) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
