from collections import deque
m,n= map(int,input().split())
box=[]
rippend=[] #0일차 익은 과일
dx=[0,0,-1,1]
dy=[1,-1,0,0]
for _ in range (n):
  box.append(list(map(int,input().split())))


def ripen(rippend):
  queue= deque()
  queue.extend(rippend)
  while queue:
    x,y= queue.popleft()
    for i in range(4):
      nx= x+ dx[i]
      ny= y+ dy[i]
      
      if(0<=nx<n and 0<=ny<m and box[nx][ny]==0):
        box[nx][ny]=box[x][y]+1 #day 하루 빼야 함.
        queue.append((nx,ny))
for i in range(n):
  for j in range(m):
    if box[i][j]==1:
      rippend.append((i,j)) #0일차 익은 과일 넣기
ripen(rippend)

result=0
for i in box:
  if 0 in i:
    result=-1 # 모두 익지 않은 경우
    break
  result= max(max(i)-1,result)

print(result)

