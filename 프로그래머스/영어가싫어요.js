function solution(numbers) {
  const num=['zero','one','two','three','four','five','six','seven','eight','nine'];
  num.forEach((number,index)=>{
      if(numbers.includes(number)) {
           numbers=numbers.replaceAll(number,index.toString())}
  })
  return Number(numbers)
}