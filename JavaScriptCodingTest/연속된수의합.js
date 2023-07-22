function solution(num, total) {
  let result=[];
  if(num%2===1){
      for(let i=0; i<num; i++){
          result.push((parseInt(total/num) - parseInt(num/2))+i)
      }
  }
  else{
      for(let i=0; i<num; i++){
          result.push(parseInt(total/num)-(parseInt(num/2)-1)+i)
      }
  }
  return result;
}