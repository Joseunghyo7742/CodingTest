function solution(s1, s2) {
  var answer = 0;
  s1.forEach(str=> s2.includes(str)? answer++: 0)
  return answer;
}


function solution(s1,se){
  const intersection = s1.filter((x)=>s2.includes(x));
  return intersection.length
}