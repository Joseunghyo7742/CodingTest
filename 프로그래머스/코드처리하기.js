function solution(code) {
  let ret='';
  let mode=0;
  for(let i=0; i<code.length; i++){
      if(mode===0){
          code[i]==1 ? mode=1 : i%2===0 ? ret+=code[i] : mode=0;
      }
      else{
          code[i]==1 ? mode=0 : i%2!==0 ? ret+=code[i] : mode=1;
      }
  }
  return ret.length ? ret : "EMPTY";
}