function solution(lines) {
  let arr= new Array(200).fill(0);
  let min= 100
  let max= -100
  let result=0
  for(let [s,e] of lines) {
      s+=100
      e+=100
      if(s<=min) min=s
      if(e>=max) max=e
      for(let i=s; i<e; i++)
          arr[i]++
  }
  for(let i=min; i<=max; i++){
      
      if(arr[i]>=2) result++
  }
  return result
}