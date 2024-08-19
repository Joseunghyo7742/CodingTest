function solution(n) {
  let count=0
  let i=1
  while(count!=n){
      if(i%3!==0 && !(i+'').includes('3')) count++;
      i++
  }
  return i-1
      
}