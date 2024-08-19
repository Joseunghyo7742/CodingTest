function solution(sizes) {
  let large_side=1
  let small_side=1
  sizes.forEach(([v,h])=>{
      if(v>h){
          if(v>large_side) large_side=v
          if(h>small_side) small_side=h
      }
      else{
          if(h>large_side) large_side=h
          if(v>small_side) small_side=v
      }
  })
  return large_side*small_side
}