#!/usr/bin/node
const script = 'C is fun';
const args = process.argv;
const x = Number(args[2]);
let i = 0;
if (Number.isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  while (i < x) {
    console.log(script);
    i++;
  }
}
