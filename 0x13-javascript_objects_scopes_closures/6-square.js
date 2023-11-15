#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let idx = 0; idx < this.height; idx++) {
      let sid = '';
      for (let j = 0; j < this.width; j++) {
        sid += c;
      }
      console.log(sid);
    }
  }
}

module.exports = Square;
