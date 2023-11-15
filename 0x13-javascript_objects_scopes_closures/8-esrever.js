#!/usr/bin/node
exports.esrever = function (list) {
  let size = list.length - 1;
  let idx = 0;
  while ((size - idx) > 0) {
    const flip = list[size];
    list[size] = list[idx];
    list[idx] = flip;
    idx++;
    size--;
  }
  return list;
};
