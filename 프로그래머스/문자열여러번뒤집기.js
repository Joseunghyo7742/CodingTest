function solution(my_string, queries) {
  let result= my_string.split(''); //문자열은 변경할 수 없으니 배열로 만드러준다.
  queries.forEach(([start,end])=>{
      console.log("s:",s,"e:",e)
      for(let i=start; i<(start+end)/2 ; i++)
          [result[i],result[start+end-i]]= [result[start+end-i],result[i]];
  })
  return result.join('')
}


function solution(my_string, queries) {
    let str = my_string.split('');
  queries.forEach(([start, end]) => {
    const changeStr = str.slice(start, end + 1);
    str.splice(start, changeStr.length, ...changeStr.reverse());
    //splice(start, length, change)- start인덱스부터, length만큼, change로 바꾼다.  
    //reverse()로 배열을 역순으로 한 후, ...전개하여 splice.j
  });
  return str.join('');
}
