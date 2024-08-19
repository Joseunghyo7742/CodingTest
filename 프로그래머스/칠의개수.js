function solution(array) {
  const str=array.join('')
  var answer = 0;

  for(let c of str){
      if(c==='7') answer++
  }
  return answer;
}

function solution(array) {
  return array.join('').split('7').length-1;
}