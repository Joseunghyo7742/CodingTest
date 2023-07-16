//바꾸기 전.
function solution(polynomial) {
  let arr = polynomial.split(" ");
  let x= 0
  let num= 0
  for(const char of arr){
      if(char.includes('x'))
          char.length===1 ? x+= 1 : x+= Number(char.slice(0,char.length-1));
      else if(char!==" " && char !== "+")
          num+= Number(char)
  }
  if( x===0 && num !== 0) return num+"";
  else if (x>1 && num===0) return x+"x";
  else if (x===1 && num===0) return "x";
  else if (x===1 && num!==0) return `x + ${num}`;
  else return `${x}x + ${num}`;
}