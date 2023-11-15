#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let idx = 0; idx < this.height; idx++) {
      let sid = '';
      for (let j = 0; j < this.width; j++) {
        sid += 'X';
      }
      console.log(sid);
    }
  }
}

module.exports = Rectangle;
