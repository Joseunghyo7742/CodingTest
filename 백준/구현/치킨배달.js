//nxn 도시, 빈칸, 치킨집 중 하나.
//도시의 칸은 (r행,c열)  1부터 시작
// 치킨거리는 집과 가장 가까운 치킨집 사이의 거리
//도시의 치킨거리: 모든 집의 치킨거리 합
//0 빈칸, 1 집, 2 치킨집
//M<=치킨집 <13, 치킨집 최대 m개 골랐을 때 도시의 치킨거리 최솟값
//최대 폐업시키지않을 치킨집 M개

const fs = require('fs');

const [nm, ...arr] = fs
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
  )
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.trim().split(' ').map(Number));

const [n, m] = nm;

function getCombination(arr, select) {
  const results = [];
  if (select === 1) return arr.map((e) => [e]);

  arr.forEach((e, i, o) => {
    const rest = o.slice(i + 1);
    const combinations = getCombination(rest, select - 1);
    const attached = combinations.map((r) => [e, ...r]);
  });
  results.push(...attached);
}

const houses = [];
const stores = [];

for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (arr[i][j] === 1) {
      houses.push([i, j]);
    } else if (arr[i][j] === 2) {
      stores.push([i, j]);
    }
  }
}
let len = Array.from({ length: chicken.length }, (_, i) => i);
let comb = getCombination(len, m);

let cost = [];

comb.forEach((e) => {
  let total = 0;
  for (let [a, b] of home) {
    let check = 99999999999;
    e.forEach((r) => {
      let d = Math.abs(chicken[r][0] - a) + Math.abs(chicken[r][1] - b);
      if (check > d) check = d;
    });
    total += check;
  }
  cost.push(total);
});
console.log(Math.min(...cost));
