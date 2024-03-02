const fs = require('fs').readFileSync(
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
);
const input = fs.toString().trim().split('\n');
const count = Number(input[0]);
const map = input.slice(1).map((el) => el.split('').map(Number));

const dx = [0, 0, 1, -1];
const dy = [1, -1, 0, 0];
let dangi = [];
let cnt = 1;
//dfs 함수만들기
function dfs(x, y) {
  for (let i = 0; i < 4; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];

    if (nx < 0 || nx >= count || ny < 0 || ny >= count) {
      continue;
    }
    if (map[nx][ny] == 1) {
      map[nx][ny] = 2;
      cnt++;
      dfs(nx, ny);
    }
  }
}
for (let i = 0; i < count; i++) {
  for (let j = 0; j < count; j++) {
    if (map[i][j] == 1) {
      map[i][j] = 2;
      dfs(i, j);
      dangi.push(cnt);
      cnt = 1;
    }
  }
}
console.log(dangi.length);
dangi.sort((a, b) => a - b);
dangi.forEach((n) => console.log(n));

//output: 총 단지 수, 각 단지별 세대 수. =>DFS
