#!/usr/bin/node

const Rectangle = require('./4-rectangle');

/* class Square */

class Square extends Rectangle {i
  constructor (size) {
  super (size, size);
  }  
}

module.exports = Square;
