function solution(s, n) {
  const small='abcdefghijklmnopqrstuvwxyz'
  const big='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  var answer = '';
  [...s].forEach((char)=>{
      if(char===' ')
          answer+=char
      else if(65<=char.charCodeAt(0)&& char.charCodeAt(0) <=90){
          answer+=big[(big.indexOf(char)+n)%26]
      }
      else {
          answer+=small[(small.indexOf(char)+n)%26]
      }
          
      
  })
  return answer;
}

function solution(s, n) {
  var chars = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXY                          "
  return s.split('').map(e => chars[chars.indexOf(e)+n]).join('');
}
//indexof는 해당하는 원소의 첫번쨰 인덱스만 출력하니까