const fs = require('fs');

const input = fs
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
  )
  .toString()
  .trim()
  .split('\n');

let index = 0;

const dy = [-1, -1, -1, 0, 0, 1, 1, 1];
const dx = [-1, 0, 1, -1, 1, -1, 0, 1];

function dfs(y, x, map, w, h) {
  map[y][x] = 0;
  for (let i = 0; i < 8; i++) {
    const ny = y + dy[i];
    const nx = x + dx[i];
    if (ny < 0 || nx < 0 || ny >= h || nx >= w) continue;
    if (map[ny][nx] === 1) dfs(ny, nx, map, w, h);
  }
}

let result = []; //섬 개수

while (true) {
  //첫 줄엥 너비와 높이를 읽음
  let [w, h] = input[index++].split(' ').map(Number);
  if (w === 0 && h === 0) break; // 0 0 이면 종료

  //지도 데이터 읽기
  let map = [];
  for (let i = 0; i < h; i++) {
    map.push(input[index++].split(' ').map(Number));
  }
  let count = 0;
  for (let j = 0; j < h; j++) {
    for (let k = 0; k < w; k++) {
      if (map[j][k] === 1) {
        count++;
        dfs(j, k, map, w, h);
      }
    }
  }
  result.push(count);
}
console.log(result.join('\n'));
