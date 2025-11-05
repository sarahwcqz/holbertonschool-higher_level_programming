#!/usr/bin/node
function facto (a) {
  if (Number.isNaN(a) || a <= 1) {
    return 1;
  }
  return a * facto(a - 1);
}

const args = process.argv;
const number = parseInt(args[2]);
console.log(facto(number));
