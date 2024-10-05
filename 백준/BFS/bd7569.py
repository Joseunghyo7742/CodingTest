from collections import deque
m,n,z= list(map(int,input().split()))

box=[]
# 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸

dr=[0,0,-1,1]
dc=[1,-1,0,0]

def bfs(q):
  day=0
  while(q):
    day+=1
    for i in range(len(q)):
      h,r,c= q.popleft()
      for i in range(4):
        nr= r+dr[i]
        nc= c+dc[i]
        if(nr<0 or nr>=n or nc<0 or nc>=m):
          continue
        elif(box[h][nr][nc]==0):
          box[h][nr][nc]=1
          q.append([h,nr,nc])
      if(h-1>=0 and box[h-1][r][c]==0):
        box[h-1][r][c]=1
        q.append([h-1,r,c])
      if(h+1<z and box[h+1][r][c]==0):
        box[h+1][r][c]=1
        q.append([h+1,r,c])
  return day   

        
q= deque()
allR=True
for i in range(z):
  floor=[]
  for j in range(n):
    line= list(map(int,input().split()))
    if(0 in line): allR=False
    floor.append(line)
  box.append(floor)
  
  
if(allR): #모두 익었을 때
  print(0)
  exit()

for i in range(z):
  for j in range(n):
    for k in range(m):
      if(box[i][j][k]==1):
        q.append([i,j,k])




result= bfs(q)

for i in range(z):
  for j in range(n):
    for k in range(m):
      if(box[i][j][k]==0):
        print(-1)
        exit()
print(result-1)
