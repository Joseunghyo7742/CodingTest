//그래프 표현방식
// 인접행렬
const INF = Infinity; //무한대를 이용해 연결되지 않은 노드를 표현
const graph = [
  [0, 7, 5],
  [7, 0, INF],
  [5, INF, 0],
];
console.log(graph);

//인접리스트
const grpah = Array.from(Array(3), () => []);
//[노드, 거리] 형식으로 저장
graph[0].push([1, 7]);
graph[0].push([2, 5]);
grpah[1].push([0, 7]);
graph[2].push([0, 5]);

//or
// const graph=[
//   [[1,7],[2,5]]
//   [[0,7]],
//   [[0,5]]
// ]

//!! DFS
/* 
- 스택이용 -> 재귀함수이용
- 탐색 수행 시 O(n)시간복잡도

동작 과정
1. 탐색 시작 노드를 스택에 삽입하고 방문처리
2. 스택의 최상단 노드의 인접 노드 확인
  - 방문하지 않은 인접 노드가 있으면, 그 인접 노드를 스택에 넣고 방문처리
  - 방문하지 않은 인접 노드가 없다면, 스택에서 최상단 노드 꺼내기
3. 2번 과정을 더이상 수행할 수 없을 때까지 반복 
*/

const dfs = (graph, start, visited) => {
  //1. 탐색 시작 노드 방문처리
  visited[start] = true;

  //2. 탐색 노드의 인접 노드 확인
  for (const cur of graph[start]) {
    if (!visited[cur]) {
      dfs(graph, cur, visited);
    }
  }
};
let graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5]];
let visited = [...Array(5).fill(false)];
dfs(graph, 1, visited);

//!BFS
/*
 - 큐 이용
 - 탐색 수행시 O(n)의 시간 복잡도
 - 탐색 시작 노드를 큐에 삽입하고 방문 처리
 - 큐에서 노드를 전개, 해당 노드의 인접 노드 중 방문하지 않는 노드를 모두 큐에 넣고 방문 처리
 - 큐는 push()와 shift()를 이용해 구현할 수 있으나. shift()는 O(n)의 시간복잡도를 가지기 때문에
 많은 데이터를 빠르게 관리하려면 연결리스트(객체)로 큐를 구현해 사용하는게 좋다
 - 객체를 사용하면 원소의 추가, 삭제 연산을 O(1)시간에 해결할 수 있다 
 */

function BFS(graph, start) {
  let visited = [];
  let needVisit = [];

  needVisit.push(start);

  //needVisit이 빌 때까지 반복
  while (needVisit.length !== 0) {
    //needVisit의 첫 요소를 제거 후 방문할 노드로 지정
    const node = needVisit.shift();
    if (!visited.includes(node)) {
      visited.push(node);
      needVisit = [...needVisit, ...graph[node]]; //needVisit배열 뒤에 현재 노드의 인접 노드들을 추가
    }
  }
  return visited;
}
console.log(BFS(graph, 'A'));

/////

const bfs = (graph, start, visited) => {
  const q = [];
  q.push(start);
  visited[start] = true;

  while (q.length !== 0) {
    const v = q.shift();
    console.log(v);

    for (const cur of graph[v]) {
      if (!visited[cur]) {
        q.push(cur);
        visited[cur] = true;
      }
    }
  }
};
let graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7],
];

let visited = [...Array(9).fill(false)];

bfs(graph, 1, visited);
