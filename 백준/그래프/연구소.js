//빈칸:0, 벽:1, 바이러스:2, 2<=바이러스<=10 /  3<=빈칸/ 벽은 3개 세움 / 안전영역 최대 크기
const fs = require('fs');
const [size, ...map] = fs
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
  )
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.trim().split(' ').map(Number));

const [n, m] = size;

const dy = [-1, 0, 1, 0];
const dx = [0, 1, 0, -1];
function bfs(map) {
  const q = [];
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (map[i][j] === 2) q.push([i, j]);
    }
  }
  while (q.length !== 0) {
    const [y, x] = q.shift();
    for (let i = 0; i < 4; i++) {
      const ny = y + dy[i];
      const nx = x + dx[i];
      if (0 <= ny && ny < n && 0 <= nx && nx < m && map[ny][nx] === 0) {
        map[ny][nx] = 2;
        q.push([ny, nx]);
      }
    }
  }
}
//0의 개수 세기 
function countBlanks(arr) {
  let count = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (arr[i][j] === 0) {
        count += 1;
      }
    }
  }
  return count;
}

let result = 0;

//벽세우기 전략이 생각나지않으면 그냥 하나씩 다 세워보자 
//벽세우기 재귀함수 
function makeWall(count) {
  if (count === 3) {
    //맵 깊은 복사 
    const copy_map = map.map((row) => [...row]);
    bfs(copy_map); 
    result = Math.max(result, countBlanks(copy_map));
    return;
  }
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (map[i][j] === 0) {
        map[i][j] = 1;
        makeWall(count + 1); //재귀함수 
        map[i][j] = 0; //맵 원상복구
      }
    }
  }
}
makeWall(0);

console.log(result);
