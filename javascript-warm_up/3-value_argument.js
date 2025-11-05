#!/usr/bin/node
const args = process.argv;
const arg2 = args[2];
if (arg2) {
  console.log(arg2);
} else {
  console.log('No argument');
}
