#!/usr/bin/node

exports.converter = function (log) {
  return function (digit) {
    return digit.toString(log);
  };
};
