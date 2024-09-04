const fs = require('fs').readFileSync(
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
);
const input = fs.toString().trim().split('\n').map(Number);

const [n, ...arr] = input;

function solve1() {
  // 산술평균 : N개의 수들의 합을 N으로 나눈 값
  const result = arr.reduce((acc, curr) => acc + curr);
  return Math.floor(result / n);
}
function solve2() {
  // 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
  //중앙값 구하기
  const temp = arr.sort((a, b) => a - b);
  const middleIdx = Math.floor(n / 2);
  return temp[middleIdx];
}
function solve3() {
  let map = new Map();
  arr.forEach((e) => map.set(e, (map.get(e) || 0) + 1));
  map = [...map].sort((a, b) => b[1] - a[1]); //값 기준으로 내림차순 정렬
  // 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
  // [[3,3],[2,3],[1,3]]
  if (map.length === 1 || map[0][1] > map[1][1]) return map[0][0]; //값이 하나거나, 최빈값이 유일할 때
  let temp = map.filter((el) => el[1] === map[0][1]);
  temp.sort((a, b) => a[0] - b[0]);
  return temp[1][0];
}
function solve4() {
  // 전체 범위 출력
  const min = Math.min(...arr);
  const max = Math.max(...arr);
  return max - min;
}

console.log(solve1());
console.log(solve2());
console.log(solve3());
console.log(solve4());
