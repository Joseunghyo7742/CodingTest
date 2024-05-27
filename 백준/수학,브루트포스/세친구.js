const fs = require('fs');
const [info, ...rel] = fs
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
  )
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.trim().split(' ').map(Number));

const [n] = info; //사람 수 n, 관계 수 m

let friendsList = Array.from(Array(n + 1), () => []); //빈 배열 N+1개 [ [], [], [], ...]

for (const [a, b] of rel) {
  friendsList[a].push(b);
  friendsList[b].push(a);
}

//하나씩 돌기. length가 1이하면 무시

// 두 가지 선택 -> 예를 들어 (a,b)선택. a,b 중 a내에 b가 있거나 b 내에 a가 있다면 성공
let answer = Infinity;

friendsList.forEach((A_friends, i) => {
  if (A_friends.length < 2) return;
  for (let i = 0; i < A_friends.length; i++) {
    const B = A_friends[i];
    const B_friends = friendsList[B];
    const AB_friends = A_friends.filter((p) => B_friends.includes(p));
    AB_friends.forEach((C) => {
      const C_friends = friendsList[C];
      const friends_sum =
        A_friends.length + B_friends.length + C_friends.length - 6;
      if (friends_sum < answer) answer = friends_sum;
    });
  }
});
console.log(answer === Infinity ? -1 : answer);
