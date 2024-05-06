const fs = require('fs');
const input = fs
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
  )
  .toString()
  .trim()
  .split('\n')
  .map(Number);
const error_message = "Goldbach's conjecture is wrong.";

//소수 판별 함수
function isDecimal(num) {
  //제곱근보다 낮은 홀수로만 나눠보기
  for (let i = 3; i < parseInt(Math.sqrt(num)); i += 2) {
    if (num % i === 0) return false;
  }
  return true;
}

// for (const num of input) {
//   if (num === 0) break;
//   else {
//     //절반 이하의 홀수는 순서만 바뀌는 거기 때문에 보지않음
//     for (let i = num - 3; i >= num / 2; i -= 2) {
//       if (isDecimal(i) && isDecimal(num - i)) {
//         console.log(`${num} = ${num - i} + ${i}`);
//         break;
//       }
//     }
//   }
// }
let idx = 0;
while (input[idx] !== 0) {
  const num = input[idx];
  let check = false;
  for (let i = num - 3; i >= num / 2; i -= 2) {
    if (isDecimal(i) && isDecimal(num - i)) {
      console.log(`${num} = ${num - i} + ${i}`);
      check = true;
      break;
    }
  }
  idx += 1;
  if (!check) {
    console.log(error_message);
  }
}
