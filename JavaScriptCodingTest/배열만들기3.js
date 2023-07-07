function solution(arr, intervals) {
  let answer=[];
  intervals.forEach(([s,e])=>{
    //answer.push(...arr.slice(s,e+1))

      for(let i=s; i<=e; i++){
          answer.push(arr[i])
          
      }
  })
                    
  return answer;

  function solution(arr, intervals) {
    const [[a,b],[c,d]] = intervals;

    return [...arr.slice(a, b+1), ...arr.slice(c, d+1)];
}