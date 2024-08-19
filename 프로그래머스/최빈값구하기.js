function solution(array) {
  const num= new Map();
  
  for(let n of array){
      if(!num.has(n)) num.set(n,0); //처음만난 수, Map에 추가
      if(num.has(n)) num.set(n,num.get(n)+1);//Map에 있을 경우 카운트+1
  }
  let sorted= [...num].sort((a,b)=> b[1]-a[1])//value를 기준으로 내림차순정렬
  if(sorted.length>1 && sorted[0][1]===sorted[1][1]) return -1 //최빈값이 여러개인 경우
  else return sorted[0][0];
}