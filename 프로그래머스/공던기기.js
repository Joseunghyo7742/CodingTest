function solution(numbers, k) {
  let count=1
  let index=0
  while(count!=k){
      index=(index+2)%numbers.length
      count++
  }
  return numbers[index]
}

function solution(numbers, k) {

  return numbers[((2 * (k -1))) % numbers.length];
}