#!/usr/bin/node

exports.esrever = function (list) {
  let length = list.length - 1;
  const rArray = [];
  let i = 0
  while (i < list.length && length >= 0) {
    rArray[i] = list[length];
    i += 1;
    length -= 1;
  }
  return (rArray);
}
