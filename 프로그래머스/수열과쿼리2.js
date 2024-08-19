function solution(arr, queries) {
  var answer = [];
  queries.forEach(([s,e,k])=>{
      let target=1000001;
      for(let i=s; i<=e; i++){
          if(arr[i]>k && arr[i]<=target) {
              target=arr[i]
          }
      }
      if(target===1000001) target=-1
      answer.push(target)
  })
  return answer;
}

function solution (arr, queries) {
  return queries.map(([s,e,k])=>{
    let result=-1
    for( let i=s; i<=e; i +=1){
      const v= arr[i]
      if(v<=k) continue
      result= result=== -1 ? v: Math.min(result,v)
    }
    return result
  })

}