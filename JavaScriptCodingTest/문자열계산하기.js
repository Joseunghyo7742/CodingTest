function solution(my_string) {
  var answer = BigInt(my_string[0])
  for(let i=1; i<my_string.length; i++){
      if(my_string[i]==="+")
          answer+= BigInt(my_string[i+=2])
      if(my_string[i]==='-') answer-=BigInt(my_string[i+=2])
  }
  return answer;
}