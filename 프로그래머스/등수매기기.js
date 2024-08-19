function solution(score) {
  let avg= score.map(arr=> (arr[0]+arr[1])/2);
  let answer=new Array(score.length).fill(1);
  for( let i=0; i< avg.length; i++)
      for(let j=0; j<avg.length; j++)
          if(avg[i]<avg[j]) answer[i]++
  return answer
}
//자기보다 순위가 높은사람 +1



function solution(score) {
    let avg = score.map(v=>(v[0]+v[1])/2);
    let sorted = avg.slice().sort((a,b)=>b-a);
    return avg.map(v=>sorted.indexOf(v)+1); //indexOf는 처음 일치하는 값의 인덱스를 반환하니까 중복된 값이어도 인덱스 값은 동일함.
}