#!/usr/bin/node
const SquareF = require('./5-square.js');
class Square extends SquareF {
  charPrint (x = 'X') {
    let rect = '';
    let i;
    for (i = 0; i < this.width; i++) rect += x;
    // print Rectangle

    for (i = 0; i < this.height; i++) console.log(rect);
  }
}
module.exports = Square;
