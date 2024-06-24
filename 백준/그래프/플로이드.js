const fs = require('fs');
//도시 개수 n, 버스 개수 m/ 버스 정보
// 출발 도시 번호- (시작도시, 도착도시, 비용)

let [n, m, ...arr] = fs
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
  )
  .toString()
  .trim()
  .split('\n');

arr = arr.map((bus) => bus.trim().split(' ').map(Number));
n = Number(n.trim());
m = Number(m.trim());
const costMap = Array.from(new Array(n + 1), () => new Array(n + 1).fill(0));

//일단 비용입력
arr.forEach((bustInfo) => {
  const [start, end, cost] = bustInfo;
  if (costMap[start][end] === 0 || costMap[start][end] > cost) {
    costMap[start][end] = cost;
  }
});

//하나씩 최소비용으로 갱신가능한지 검사
function getMinCost(start, cost) {
  
}
//0이 아니라면 bfs에 넣기
//bfs에선 도착 목적지인덱스이면 최소비용 비교 후 갱신
// 도착 목적지인덱스가 아니라면 큐에 넣기
