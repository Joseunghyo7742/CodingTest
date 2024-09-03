const fs = require('fs');

const [num, ...arr] = fs
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
  )
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.trim().split(' ').map(Number));

const [n, m] = num;

const map = arr.slice(0, n);
const prefixSum = Array.from(Array(n), () => Array(n).fill(0));

prefixSum[0][0] = map[0][0];
for (let i = 0; i < n; i++) {
  if (i > 0) {
    prefixSum[i][0] = map[i][0] + prefixSum[i - 1][n - 1];
  }
  for (let j = 1; j < n; j++) {
    prefixSum[i][j] = map[i][j] + prefixSum[i][j - 1];
  }
}

let result = [];
for (let i = n; i < n + m; i++) {
  const [x1, y1, x2, y2] = arr[i];
  const sum = prefixSum[x2 - 1][y2 - 1] - prefixSum[x1 - 1][y1 - 1];
  result.push(sum);
}
console.log(result);
