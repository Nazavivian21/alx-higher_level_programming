#!/usr/bin/node
const baseSquare = require('./5-square');

class Square extends baseSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
