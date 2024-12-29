# 두 덩어리 이상으로 분리되는 최초의 시간(년)

# --함수의 목적--
#- 년도를 카운트한다.
# 1. 1년마다 인접한 바다로 인해 빙산의 높이를 줄인다. 이떄 0이하로 내려가진 않음
# 2. 빙산 덩어리 개수 카운트 => 두 덩어리 이상이 되면 지난 년도를 반환한다.
# 다 녹았는데도 섬이 두개 이상 안생기면 0
from collections import deque

n,m = list(map(int, input().split()))
iceberg=[]

for _ in range(n):
  iceberg.append(list(map(int,input().split())))


dr=[0,0,-1,1]
dc=[-1,1,0,0]

def getNewIceberg():
  newIceberg=[[0 for _ in range(m)] for _ in range(n)]
  for i in range(n):
    for j in range(m):
      if(iceberg[i][j]!=0):
        temp= iceberg[i][j]
        for k in range(4):
          nr=i+dr[k]
          nc=j+dc[k]
          if(iceberg[nr][nc]==0 and temp>0):
            temp-=1
        newIceberg[i][j]=temp
        
  return newIceberg

def getCountIceberg(r,c):
  q= deque()
  q.append([r,c])
  while(q):
    r,c= q.popleft()
    for i in range(4):
      nr=r+ dr[i]
      nc=c+ dc[i]
      if(nr<0 or nr>=n or nc<0 or nc>=m):
        continue
      if(iceberg[nr][nc]!=0 and check[nr][nc]==0):
        check[nr][nc]=1
        q.append([nr,nc])
  

result=0 #년도
while(True):
  result+=1
  iceberg=getNewIceberg()
  
  count=0
  check=[[0 for _ in range(m)] for _ in range(n)]
  for i in range(n):
    for j in range(m):
      if(check[i][j]==0 and iceberg[i][j]!=0):
        count+=1
        getCountIceberg(i,j)
  if(count==0):
    result=0
    break
  elif(count>=2):
    break

print(result)
  

  

