function solution(my_string) {
  let arr= my_string.split(' ')
  let answer= Number(arr[0])
  for(let i=1; i<arr.length; i++)
  {
      if(arr[i]==='+'){
          answer+=Number(arr[++i])
      }
      if(arr[i]==='-')
          answer-=Number(arr[++i])
  }
  return answer
}

//자릿수를 고려했어야함