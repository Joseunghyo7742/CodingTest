function solution(dots) {
  dots.sort((a,b)=> a[0]-b[0]) //x축 기준 오름차순정렬
  
  const column= Math.abs(dots[0][1]-dots[1][1])
  const row= Math.abs(dots[0][0]-dots[3][0])
  
  return column*row;
}