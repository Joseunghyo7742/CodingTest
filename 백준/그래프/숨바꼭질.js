const fs = require('fs');
const [nm, ...ms] = fs
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
  )
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.trim().split(' ').map(Number));

const [n, m] = nm;
const check = Array.from({ length: n + 1 }).fill(0);
const graph = Array.from({ length: n + 1 }, () => []);

ms.forEach(([u, v]) => {
  graph[u].push(v);
  graph[v].push(u);
});

