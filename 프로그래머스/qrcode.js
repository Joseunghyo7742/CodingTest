function solution(q, r, code) {
  let result=[]
  code.split('').forEach((char,index)=>{
      if(index%q===r) result.push(char)
  })
  // [...code].map((v, idx) => idx % q === r ? answer += v : answer)
  // return [...code].filter((_, i) => i % q === r).join('');
  return result.join('')
}