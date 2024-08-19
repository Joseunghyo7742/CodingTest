function solution(my_string) {
  let answer=new Array(52).fill(0);
  for(let i=0; i<my_string.length; i++){
      let index= my_string.charCodeAt(i)-65;
      if(index>=32) index-=6
      answer[index]+=1
  }
  return answer;
}

function solution(my_string){
  const alp="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
  let answer= new Array(52).fill(0);
  for( let i=0; i<my_string.length; i++){
    answer[alp.indexOf(my_string[i])]++;
  }
  return answer;
}