const fs = require('fs');
const [info, ...B] = fs
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
  )
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.trim().split(' ').map(Number));

const [h, w, x, y] = info;
const A = Array.from({ length: h }, () => Array(w).fill(0));

for (let i = 0; i < h; i++) {
  for (let j = 0; j < w; j++) {
    A[i][j] = B[i][j];
  }
}
for (let i = x; i < h; i++) {
  for (let j = y; j < w; j++) {
    A[i][j] = B[i][j] - A[i - x][j - y];
  }
}

for (let k = 0; k < h; k++) {
  console.log(A[k].join(' '));
}
