function solution(arr, k) {
  let set= new Set(arr);
  let result=[...set];
  if(result.length<k){
      while(result.length!==k){
          result.push(-1)
      }
      return result
  }
  return result.slice(0,k)
  
  
}
function solution (arr,k){
  const set= new Set(arr);
  return set.size < k ? [...set, ...Array(k-set.size).fill(-1)] : [...set].slice(0,k);
}