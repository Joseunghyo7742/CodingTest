function solution(my_str, n) {
  var answer = [];
  
  for(let i=0; i<my_str.length; i+=n){
      answer.push(my_str.substring(i,i+n)); //문자열길이를 초과하면 끝길이까지만 하는 듯
  }
  let temp= (my_str.length/n)*n
  return answer;
}