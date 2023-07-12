function solution(my_string) {
  var answer = '';
  for( let i=0; i<my_string.length; i++){
      if(answer.includes(my_string[i])) continue
      answer+=my_string[i]
  }
  return answer;
}

function solution(my_string){
  return [... new Set(my_string)].join('');
}