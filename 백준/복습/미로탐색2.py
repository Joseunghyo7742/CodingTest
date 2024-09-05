
from collections import deque

n,m = map(int, input().split()) # map(값 타입, 적용할 값 )
maze=[]
for i in range(n):
  maze.append(list(map(int, input()))) #map객체 [1,2,3]을 list로 변환 
  
#방향 적기
d_x=[0,1,0,-1] 
d_y=[1,0,-1,0]

def bfs(y,x):
  queue= deque()
  queue.append((y,x))
  
  while queue:
    y,x= queue.popleft()
    for i in range(4):
      n_y= y+ d_y[i]
      n_x= x+ d_x[i]
      if(n_y<0 or n_y >=n or n_x<0 or n_x>=m):
        continue
      if maze[n_y][n_x]==0:
        continue
      if(maze[n_y][n_x]==1):
        maze[n_y][n_x] = maze[y][x] +1
        queue.append( (n_y, n_x))
  return maze[n-1][m-1]

print(bfs(0,0))