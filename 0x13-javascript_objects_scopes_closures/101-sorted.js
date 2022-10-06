#!/usr/bin/node

const dict = require('./101-data.js').dict;
const nDict = {};
const key = Object.keys(dict);
const unsortedValues = Object.values(dict);
const value = [...new Set(unsortedValues)];

for (let i = 0; i < value.length; i++) {
  const nArray = [];
  for (let j = 0; j < key.length; j++) {
    if (dict[key[j]] === value[i]) nArray.push(key[j]);
    nDict[value[i]] = nArray;
  }
}
console.log(nDict);
