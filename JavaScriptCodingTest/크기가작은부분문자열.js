function solution(t, p) {
  let answer=[];
  for(let i=0; i+(p.length-1)<t.length; i++)
      answer.push(Number(t.slice(i,i+p.length)))
  
  return answer.filter(n=>n<=Number(p) ).length
}