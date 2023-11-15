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

  rotate () {
    const flip = this.width;
    this.width = this.height;
    this.height = flip;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
