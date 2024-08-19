function solution(quiz) {
  var answer = [];        
  for(const q of quiz){
      let quiz_arr= q.split(" "); //공백 기준으로 배열에 나눠담기
      const [x,op,y, ,z]=quiz_arr; //=을 제외하고 구조분해할당
      if(op==="+")
          Number(x)+Number(y)===Number(z) ? answer.push("O") : answer.push("X");
      else
          Number(x)-Number(y)===Number(z) ? answer.push("O") : answer.push("X");
  }
  return answer;
}