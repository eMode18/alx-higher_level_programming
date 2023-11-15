#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  let myArr = process.argv.slice(2).map(Number);
  let next = myArr.sort(function (a, b) { return b - a; })[1];
  console.log(next);
}
