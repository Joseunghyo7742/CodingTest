function solution(arr) {
  let result=[]
  arr.forEach((num)=>{
      if(num>=50 && num%2===0)
          result.push(num/2)
      else if(num<50 && num %2 !==0)
           result.push(num*2)
      else
          result.push(num)
  })
  
  return result;
}

function solution(arr){
  return arr.map(num=>{
    if(num>=50 && !(num%2)) return num/2;
    if(num<50 && num%2) return num*2;
    return num;
  })
}