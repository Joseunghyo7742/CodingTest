function solution(arr) {
    //const diff= Math.abs(arr[0].length- arr.length);
  if(arr[0].length>arr.length) { //열의 길이가 더 길 때
      const diff= arr[0].length-arr.length
      for(let i=0; i<diff; i++) {
          const a = new Array(arr[0].length).fill(0);
          arr.push(a);
          console.log("반복")
      }
          
  }
  else if(arr[0].length <arr.length){ //행의 길이가 더 길 때
      const diff= arr.length-arr[0].length
      arr.forEach(num => {
          for(let i=0; i< diff; i++) num.push(0);
      })
  }
  return arr;
}