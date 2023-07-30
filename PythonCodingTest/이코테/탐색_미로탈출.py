from collections import deque
  
n,m = map(int,input().split())

#맵 입력받기
map=[]
for i in range(n):
  map.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
  queue=deque()
  queue.append((x,y))
  
  while queue:
    x,y= queue.popleft()
    for i in range(4):
      nx= x+ dx[i]
      ny= y+ dy[i]
      #공간을 벗어났거나 벽인경우
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      if map[nx][ny]==0:
        continue
      if map[nx][ny]==1:
        map[nx][ny]= map[x][y]+1
        queue.append((nx,ny))
  return map[n-1][m-1] #가장 오른쪽 아래까지의 최단 거리 반환

print(bfs(0,0))
          

