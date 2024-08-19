
function solution(numer1, denom1, numer2, denom2) {
  var answer = [];
  let denom= denom1*denom2; //두 분모의 공배수
  let numer= (numer1*denom2) + (numer2*denom1); 
  let gcd=1 //최대공약수
  for(let i=2; i<= Math.min(denom,numer); i++){
      if(denom%i===0 && numer%i===0) gcd=i;
  }
  answer.push(parseInt(numer/gcd));
  answer.push(parseInt(denom/gcd));
  
  return answer;
}