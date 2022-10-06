#!/usr/bin/node

/* Square Class */

const S1 = require('./5-square.js');

class Square extends S1 {
  constructor (size) {
    super(size);
    this.length = size;
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.length; i++) {
        for (let j = 0; j < this.length; j++) {
          process.stdout.write(String(c));
        }
        process.stdout.write('\n');
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
