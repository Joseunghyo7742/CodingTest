
function solution(today, terms, privacies) {
  const day = 28
  const month= 12
  const yearDays= day*month
  
  var answer = [];
  
  const getDays=(date)=>{
      const dateArr= date.split(".").map(Number) //YYYY.MM.DD -> 숫자배열로 
      const totalDays= dateArr.reduce((total,e,i)=>{
          switch(i){
              case(0):
                  return total+=e*yearDays;
              case(1):
                  return total+=e*day
              case(3):
                  return total+=e
              default:
                  return e
          }
      },0)
      return totalDays
  }
      
  
  //약관유형 객체화. 
  const temp=terms.map((e)=>e.split(" "))
  const term_table= Object.fromEntries(temp) //개월수가 string으로 들어감

  //privacies를 돌면서 날짜 개월 수 계산
  privacies.forEach((priv,index)=>{
    const info= priv.split(" ")
    const created_at= info[0] 
    const type= info[1]
    
    const gapLimit = Number(term_table[type])*28 //대괄호표기법으로 찾자 . 유효기간을 일 수로 계산
    console.log("gapLimit",gapLimit)
    
    const gap = getDays(today)-getDays(created_at)
      console.log("gap",gap)
    
    if(gap>=gapLimit){
        result.append(index+1)
    }
    
    
  //약관유형에 해당하는 개월 수 인지 검사 후, 파기해야할 시 배열에 추가
  })
  
  
  return answer;
}