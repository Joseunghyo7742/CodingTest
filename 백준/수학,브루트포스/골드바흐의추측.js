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

//소수면 false
const arr = Array.from({ length: 1000001 }, () => 1); //길이가 1000000인 0인 배열 생성
for (let i = 3; i <= 499999; i += 2) {
  if (arr[i]) {
    console.log('i', i);

    for (let j = 3; i * j <= 1000001; j += 2) {
      arr[i * j] = 0;
    }
  }
}

let idx = 0;
while (input[idx] !== 0) {
  const num = input[idx];
  let check = false; //해당 짝수가 두 소수의 합으로 이뤄지는게 있는지 확인.
  for (let i = num - 3; i >= num / 2; i -= 2) {
    if (arr[i] && arr[num - i]) {
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
