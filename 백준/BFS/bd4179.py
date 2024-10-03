# #: 벽
# .: 지나갈 수 있는 공간
# J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
# F: 불이 난 공간

from collections import deque

n,m= list(map(int,input().split()))

miro=[]
for i in range(n):
  miro.append(list(input())) #str은 인덱싱으로 읽기만 가능하고 변경은 불가하니 list로 바꿔준다.

dr=[0,0,-1,1]
dc=[1,-1,0,0]



def bfs(queue):
  time=0
  flag=True
  while(queue and flag):
    time+=1
    size = len(queue)
    for i in range(size):
      r,c= queue.popleft()
      for i in range(4):
        nr= r+dr[i]
        nc= c+dc[i]
        if(nr<0 or nr>=n or nc<0 or nc>=m ):
          if(miro[r][c]=="J"): 
            flag=False
            break
          else: continue
        elif(miro[nr][nc]=="."):
          miro[nr][nc]=miro[r][c]
          queue.append([nr,nc])
  if(flag): return 0
  else: return time

q= deque()
F_loc=[]
J_loc=[]
for i in range(n):
  for j in range(m):
    if(miro[i][j]=="F"):
      F_loc.append([i,j])
    elif(miro[i][j]=="J"):
      J_loc=[i,j]

for i in F_loc: q.append(i)
q.append(J_loc)

time=bfs(q)

if(time==0): print("IMPOSSIBLE")
else: print(time)

