#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const processes = Number(process.argv[2]);
  let idx = 0;
  while (idx < processes) {
    console.log('C is fun');
    idx++;
  }
}
