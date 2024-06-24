//4를 1,2,3합으로 나타내는 7가지 방법, 1개 이상 사용
//순서 생각
//정수 n-> 1,2,3합으로 나타내는법
//3(테케수),4,7,10 -> 7,44,274
//n은 11보다 작다.
const fs = require('fs').readFileSync(
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
);
const [t, ...input] = fs.toString().trim().split('\n').map(Number);

const dp = [1, 2, 4];
for (let i = 3; i < 11; i++) {
  const new_dp = dp[i - 1] + dp[i - 2] + dp[i - 3];
  dp.push(new_dp);
}
const answer = [];
for (let i = 0; i < t; i++) {
  answer.push(dp[input[i] - 1]);
}
console.log(answer.join('\n'));
