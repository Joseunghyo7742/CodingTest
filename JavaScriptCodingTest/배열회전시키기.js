function solution(numbers, direction) {
  var answer = [];
  const n= numbers.length;
  if(direction ==='right'){
      answer.push(numbers[n-1]);
      for( let i= 0; i<n-1; i++){
          answer.push(numbers[i]);
      }
  }
  else{
      for(let i=1; i<n; i++){
          answer.push(numbers[i]);
      }
      answer.push(numbers[0]);
  }
  return answer;
}

function solution(numbers, direction) {
  var answer = [];

  if ("right" == direction) {
      numbers.unshift(numbers.pop());
  } else {
      numbers.push(numbers.shift());
  }

  answer = numbers;

  return answer;
}