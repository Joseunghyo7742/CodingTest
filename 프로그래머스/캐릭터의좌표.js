function solution(keyinput, board) {
  const direction= {up:[0,1], down: [0,-1], left: [-1,0], right:[1,0]};
  let x=0
  let y=0
  const max_x= board[1]/2
  const max_y= board[0]/2
  console.log(max_x)
  for (const key of keyinput){
      const move= direction[key]
      const new_x= x+move[1] //x+=move[1]로 하는 대입연산자 실수.
      const new_y= y+move[0]
      console.log(new_x)
      if(Math.abs(new_x)>max_x || Math.abs(new_y)>max_y) continue;
      x=new_x
      y=new_y
  }
  
  let result= [y,x]
  return result
  
}