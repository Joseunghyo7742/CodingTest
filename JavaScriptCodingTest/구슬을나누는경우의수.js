function solution(balls, share) {
  let a=1; let b=1;
  for (let i=balls; i>balls-share; i--) a*=i
  for(let j=share; j>=1; j--) b*=j
  return a/b;
}


//재귀함수식
const factorial= (n)=> n===0 ? 1: n*factorial(n-1);
function solution(balls, share){
  return Math.round(factorial(balls)/factorial(balls-share)/factorial(share))
}