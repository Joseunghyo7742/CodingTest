function solution(num_list) {
  let even='';
  let odd='';
  num_list.forEach((number)=>{
      number%2==0? even+=number: odd+=number;
  })
  
  return Number(even)+ Number(odd);
}

