function solution(picture, k) {
  let result=[];
  for(pic of picture){
      const appended= [...pic].map(c=> c.repeat(k)).join("");
      for(let i=0; i<k; i++) result.push(appended);
  }
  return result;
}