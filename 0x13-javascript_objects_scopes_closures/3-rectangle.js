#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      Object.create(null);
    }
  }

  print () {
    let rect = '';
    let i;
    for (i = 0; i < this.width; i++) rect += 'X';
    // print Rectangle

    for (i = 0; i < this.height; i++) console.log(rect);
  }
}

module.exports = Rectangle;
