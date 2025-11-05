#!/usr/bin/node
const args = process.argv;
const list = args.slice(2).map(Number);
const len = list.length;
let largest = 0;
let secondLargest = -1;

if (list.length < 2) {
    console.log(0);
} else {
    for (let i = 0; i < len; i++) {
        if (list[i] > largest) {
            largest = list[i];
        }
    }
    for (let j = 0; j < len; j++) {
        if (list[j] > secondLargest && list[j] != largest) {
            secondLargest = list[j];
        }
    }
    console.log(secondLargest);
}
