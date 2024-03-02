from collections import deque

n,m= map(int, input().split())

maze=[]
for i in range (n):
  maze.append(list(map(int,input()))) 

d_column=[0,1,0,-1] 
d_row=[1,0,-1,0]

def bfs(c,r):
  queue= deque()
  queue.append((c,r))
  
  while queue:
    c,r= queue.popleft()
    for i in range(4):
      n_column=c+d_column[i]
      n_row= r+ d_row[i]
      if(n_column<0 or n_column>=n or n_row<0 or n_row>=m):
        continue
      if maze[n_column][n_row]==0: #벽
        continue
      if(maze[n_column][n_row]==1):
        maze[n_column][n_row]= maze[c][r]+1 #비용 입력
        queue.append((n_column,n_row))
  #먼저 도착하지 않은 큐 요소들은 어차피 ==1에서 걸림.
  return maze[n-1][m-1]

print(bfs(0,0))