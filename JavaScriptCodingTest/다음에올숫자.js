function solution(common) {
  const [x,y,z]= common;
  if( y-x === z-y) { //등차수열인 경우
      const d= y-x; //공차
      return common[common.length-1]+d;
  }
  else{ //등비수열의 경우
      const d= y/x;//공비
      return common[common.length-1]*d;
  }
}