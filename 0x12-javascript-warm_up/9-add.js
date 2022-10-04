#!/usr/bin/node

/* add command line integers */

const arg = process.argv;

add = (a, b) => console.log(Number(arg[2]) + Number(arg[3]));
add();
