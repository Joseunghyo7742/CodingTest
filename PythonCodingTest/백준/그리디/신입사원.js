const fs= require('fs')
const input=fs.readFileSync(process.platform==="linux"? "/dev/stdin": __dirname+"/input.txt").toString().trim().split("\n")
let input_idx= 0;
const loop_count= Number(input[input_idx++]) //test Case count


for(let i=0; i< loop_count; i++){
//입력값: 첫째 줄 지원자 수, 둘째 줄-N 줄: 지원자 서류심사 성적, 면접 성적 순위 동석차없음
//성적 중 적어도 하나라도 다른 지원자보다 좋아야 함. 

  const HC= Number(input[input_idx++]) //지원자 수
  const ranks= []//지원자 점수 2차원 배열
  for(let j=0; j<HC; j++){
    ranks.push(input[input_idx++].split(' ').map(Number))
  }

  //첫번째 랭크를 기준으로 sort
  const sort_rank= ranks.sort((a,b)=>a[0]-b[0])

  let result=1; //카운트

  //면접랭크라도 높은지 확인
  let standard=sort_rank[0][1]
  for(let i =1; i<sort_rank.length; i++){
    if(sort_rank[i][1]<standard){
      result++
      standard= sort_rank[i][1]
    }
  }
  console.log(result)
  
}