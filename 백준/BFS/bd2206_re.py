
from collections import deque
n,m = list(map(int,input().split()))
miro=[]


check =[[[0,0] for _ in range(m)] for _ in range(n)]
# 첫번째 층은 벽을 안뚫은 상태일 때, 2층은 벽을 뚫었을 때.
for _ in range(m):
  miro.append(list(map(int,input())))

dr=[0,0,-1,1]
dc=[1,-1,0,0]
  
def bfs(r,c):
  q= deque()
  q.append([r,c,0])
  check[r][c][0]=1
    
  while(q):
    r,c,cnt= q.popleft()
    if ((r==n-1) and (c==m-1)):
      return check[r][c][cnt]

    for i in range(4):
      nr= r+ dr[i]
      nc= c+ dc[i]
      if(nr<0 or nr>=n or nc<0 or nc>=m):
        continue
      if(miro[nr][nc]==0 and check[nr][nc][cnt]==0):
        check[nr][nc][cnt]=check[r][c][cnt]+1
        q.append([nr,nc,cnt])
      elif(miro[nr][nc]==1 and cnt==0):
        check[nr][nc][1]= check[r][c][0]+1
        q.append([nr,nc,1])
  else: return -1

result= bfs(0,0)
print(result)
# 00100
# 00000
# 11110
# 00000
# 01111
