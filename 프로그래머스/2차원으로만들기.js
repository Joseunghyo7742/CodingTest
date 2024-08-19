function solution(num_list, n) {
  let answer=[];
  for(let i=0; i<num_list.length;){
      answer.push(num_list.slice(i,i+=n))
  }
  return answer;
}


function solution(num_list, n) {
    var answer = [];

    while(num_list.length) {
        answer.push(num_list.splice(0,n));
    }

    return answer;
}