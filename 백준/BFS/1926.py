'''
그림
푼 날짜: 8/9
출력: 그림 개수, 최대 넓이 
'''
from collections import deque 

dc=[[1,0],[0,1],[-1,0],[0,-1]]
q= deque()
def bfs(r,c):
  q.append([r,c])
  width=0
  while(q):
    r,c= q.popleft()
    width+=1
    for i in range(4):
      nr= r+ dc[i][0]
      nc= c+ dc[i][1]
      
      if(nr<0 or nr>=n or nc<0 or nc>=m):
        continue
      elif(pic[nr][nc]==1):
        pic[nr][nc]=0
        q.append([nr,nc])
  return width
      
    

n,m = map(int,input().split())
pic=[]
for _ in range(n):
  pic.append(list(map(int,input().split())))

max_width=0
count=0
for i in range(n):
  for j in range(m):
    if(pic[i][j]==1):
      pic[i][j]=2
      count+=1
      max_width=max(max_width,bfs(i,j))

print(count)
print(max_width)
