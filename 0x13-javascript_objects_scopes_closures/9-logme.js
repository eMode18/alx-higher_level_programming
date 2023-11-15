#!/usr/bin/node
let argNo = 0;

exports.logMe = function (item) {
  console.log(argNo + ': ' + item);
  argNo++;
};
