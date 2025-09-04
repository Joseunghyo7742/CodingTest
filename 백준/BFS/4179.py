'''
불
푼 날짜: 25.09.01
'''
from collections import deque

R,C= map(int,input().split())
miro=[]
for _ in range(R):
  miro.append(list(input().strip()))

dr=[(0,1),(1,0),(-1,0),(0,-1)]
q= deque()

J_loc=[]
for i in range(R):
  for j in range(C):
    if(miro[i][j]== "F"):
      q.append([i,j])
    if(miro[i][j]=="J"):
      J_loc=[i,j]
q.append(J_loc)

time=0
flag=True
while(q and flag):
  time+=1
  for _ in range(len(q)):
    r,c= q.popleft()
    for i in range(4):
      nr= r+dr[i][0]
      nc= c+dr[i][1]
      if(nr<0 or nr>=R or nc<0 or nc>=C ):
        if(miro[r][c]=="J"):
          flag=False
          break
        continue
      if(miro[nr][nc]=="."):
        miro[nr][nc]=miro[r][c]
        q.append([nr,nc])

if(flag):
  print("IMPOSSIBLE")
else:
  print(time)