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

//방문한 노드의 거리비용을 넣기 위한 1차원 배열
const visitCost = Array.from({ length: n + 1 }).fill(null);

//인접리스트 생성
const graph = Array.from({ length: n + 1 }, () => []);
ms.forEach(([u, v]) => {
  graph[u].push(v);
  graph[v].push(u);
});

const bfs = (graph, start, visitCost) => {
  const q = [];
  q.push(start);
  visitCost[start] = 0;

  while (q.length !== 0) { 
    const node = q.shift();
    for (const curr of graph[node]) {
      if (visitCost[curr] === null) {
        q.push(curr);
        visitCost[curr] = visitCost[node] + 1;
      }
    }
  }
};

bfs(graph, 1, visitCost);
let max = 0; //가장 거리가 먼 헛간 거리
let fartestNode; // 가장 거리가 먼 노드
let count = 1; // 같은 거리의 헛간 개수
for (let i = 1; i < n + 1; i++) {
  if (visitCost[i] > max) { // 더 먼 헛간이 나오면
    max = visitCost[i];
    fartestNode = i;
    count = 1;
  } else if (visitCost[i] === max) { //max와 같은 거리의 헛간 개수 
    count += 1;
  }
}
console.log(fartestNode, max, count);
