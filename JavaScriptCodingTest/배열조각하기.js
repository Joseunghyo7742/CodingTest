function solution(arr, query) {
  query.forEach((number)=>{
      number%2==0? arr.splice(number+1): arr.splice(0,number);
  })
  return arr;
}