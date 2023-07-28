function solution(number) {
  let result=0
  function dfs(num, sum, cnt){
      if(cnt===3 || num>=number.length) return 
      sum+=number[num]
      cnt++
      if(cnt===3 &&sum===0)
          result++
      dfs(num+1,sum,cnt)
      dfs(num+1, sum-number[num],--cnt)
  }    
  
  dfs(0,0,0)
  return result
}