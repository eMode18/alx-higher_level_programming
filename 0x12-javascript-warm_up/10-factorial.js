#!/usr/bin/node
function computeFactorial (n) {
  if (n < 0) {
    return (-1);
  }
  if (n === 0 || isNaN(n)) {
    return (1);
  }
  return (n * computeFactorial(n - 1));
}

console.log(computeFactorial(Number(process.argv[2])));
