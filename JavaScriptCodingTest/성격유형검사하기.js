function solution(survey, choices) {
  let personality= ['R','T','C','F','J','M','A','N']; //성격유형
  let p_score=[0,0,0,0,0,0,0,0]; //성격 유형별 점수
  var answer = '';
  
  choices.forEach((num,index)=>{ //
      let current_pers= survey[index]; 
      let score=0;
      if(num<4){
          current_pers= current_pers.slice(0,1);
          score= 4-num;
      }
      if(num>4){
          current_pers=current_pers.slice(1,2);
          score=num-4;
      }
      let str_index= personality.findIndex((str)=> str===current_pers); //해당 성격의 인덱스찾기
      p_score[str_index]+=score;
  })
  for(let i=0; i<8; i+=2){
      if(p_score[i]===p_score[i+1]) { //점수비교 
          answer+=personality[i];
          continue;
      } 
      p_score[i]>p_score[i+1] ? answer+=personality[i]: answer+=personality[i+1];
  }
  return answer;
}