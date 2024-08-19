function solution(rank, attendance) {
  let answer=[]
  attendance.forEach((tf, index)=>{
      if(tf){
          answer.push([rank[index],index])
      }
  })
  answer.sort(function(a,b){
      return a[0]-b[0];
  })
  const a= answer[0][1]
  const b= answer[1][1]
  const c= answer[2][1]
  return a*10000+b*100+c
  
} 