function solution(numlist, n) {
  let sorted= numlist.sort((a,b)=>{
      const d_a= Math.abs(a-n);
      const d_b= Math.abs(b-n);
      if(d_a===d_b) return b-a //거리가 같다면 큰 수부터 
      return d_a -d_b //거리 오름차순정렬
  })
  return sorted;
}

function solution (numlist,n){
  return numlist.sort((a,b)=> Math.abs(a-n)-Math.abs(b-n) ||b-a )
}