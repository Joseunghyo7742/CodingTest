function solution(A, B) {
  var answer = 0;
  A=A.split("")
  for(let i=0; i<A.length; i++){
      if(A.join("")===B) return answer;
      A.unshift(A.pop());
      answer++;
  }
  return -1;
}

let solution= (a,b)=> (b+b).indexOf(a);