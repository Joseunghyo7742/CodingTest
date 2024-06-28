const fs = require('fs');

const [num, ...arr] = fs
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
  )
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.trim().split(' ').map(Number));

const cost = Array.from({ length: num }, () => []);

cost[0].push(...arr[0]);

for (let i = 1; i < num; i++) {
  for (let j = 0; j < 3; j++) {
    const prev = cost[i - 1].filter((n, index) => index !== j);
    cost[i].push(arr[i][j] + Math.min(...prev));
  }
}
console.log(Math.min(...cost[num - 1]));
