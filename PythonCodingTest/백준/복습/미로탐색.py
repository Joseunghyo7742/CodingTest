from collections import deque

n,m= map(int, input().split())

maze=[]
for i in range (n):
  maze.append(list(map(int,input()))) 

#우,하,좌,상 순 => 탈출구는 매번 우측하단이니까 BFS를 했을 때 이 순서로 해야 좀 더 빠르게 탐색할 거라고 판단.
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
        
  return maze[n-1][m-1]

print(bfs(0,0))