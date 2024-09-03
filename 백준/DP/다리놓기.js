
const fs = require('fs');

const [num, ...arr] = fs
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
  )
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.trim().split(' ').map(Number));

let result = [];
for (const el of arr) {
  const [n, m] = el;
  const temp = Math.round(combi(m) / (combi(n) * combi(m - n)));

  result.push(temp);
}

function combi(num) {
  if (num <= 1) return 1;
  return num * combi(num - 1);
}

for (const i of result) {
  console.log(i);
}
