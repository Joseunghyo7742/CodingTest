function solution(board) {
  const danger=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
  let count=0
  for(let i=0; i<board.length; i++){
      for(let j=0; j<board[0].length; j++){
          if(board[i][j]===1) continue;
          let check= true;
          for(const d of danger){
              let x= i+ d[0]
              let y= j+ d[1]
              if(x<0 || y<0|| x>=board.length || y>=board[0].length) continue;
              if(board[x][y]===1){
                  check=false
                  break;
              } 
          }
          if(check===true)
          count++;
      }
  }
  return count;
  
}