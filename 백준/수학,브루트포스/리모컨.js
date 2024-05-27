const fs = require('fs');
const [N, n, brokens] = fs
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
  )
  .toString()
  .trim()
  .split('\n');

if (N === '100') {
  console.log(0);
}

//고장난 번호가 있는 경우
else {
  let answer = Math.abs(100 - N); //채널 100번에서 이동하는 경우
  const error_n = brokens?.split(' ') || []; //고장번호들

  for (let i = 0; i < 1000000; i++) {

    
    const str = i.toString();
    let isValid = true;

    for (let j = 0; j < str.length; j++) {
      if (error_n.includes(str[j])) {
        isValid = false;
        break;
      }
    }
    if (isValid) {
      answer = Math.min(answer, Math.abs(i - N) + str.length);
    }
  }
  console.log(answer);
}
