#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const processes = Number(process.argv[2]);
  let idx = 0;
  while (idx < processes) {
    console.log('X'.repeat(processes));
    idx++;
  }
}
