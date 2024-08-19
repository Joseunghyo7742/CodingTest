
//이게 왜 안될까
//The return statement used in this context does not actually terminate the outer forEach loop. 
//Instead, it only terminates the inner every loop and continues with the next iteration of the forEach loop.
function solution(spell, dic) {
  dic.forEach((word)=>{
      if(spell.every((w)=>word.includes(w))) return 1;
  })
  return 2;
}

function solution(spell, dic) {
  for(let i=0; i<dic.length; i++){
      if(spell.every((w)=>dic[i].includes(w))) return 1; 
  }
      return 2;
  } 

function solution(spell, dic) {
  return dic.filter(v=>spell.every(c=>v.includes(c))).length ? 1 : 2;
}