function solution(l, r) {
  let answer=[];
  for(let i=l; i<=r; i++){
      let num= i+''; 
      let check=true;
      [...num].forEach((c)=>{
          if(c!=='5' && c!=='0') check=false;
      });
      if(check) answer.push(i);
  }
  if(answer.length===0)
      answer.push(-1);
  return answer;
      
}

function solution(l, r) {
  let answer=[];
  for(let i=l; i<=r; i++){
      let str= i+'';
      if(![...str].every(x=>x==='5'|| x==='0')) continue;
      answer.push(i);
  }
  return answer.length ? answer: [-1];
      
}