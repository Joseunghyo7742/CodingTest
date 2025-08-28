'''
연구소
푼날짜: 25.08.27

안전영역 크기의 최댓값 
0 빈칸, 1은 벽, 2는 바이러스

시간 복잡도 계산 후, 괜찮을 것 같을 때 완탐을 해서라도 푼다.
'''
from collections import deque

n,m= map(int,input().split())
arr=[]
for _ in range(n):
  arr.append(list(map(int,input().split())))
    
dirc=[(-1,0),(1,0),(0,-1),(0,1)]
result=-1

viruses = [(i, j) for i in range(n) for j in range(m) if arr[i][j] == 2]

def bfs(v):
  q = deque(viruses)  # ★ 바뀐 부분: 재스캔 안 함
  # 바이러스 퍼뜨리기
  while(q):
    c,r= q.popleft()
    for k in range(4):
      nc= c+ dirc[k][0]
      nr= r+ dirc[k][1]
      if(nc<0 or nc>=n or nr<0  or nr>=m):
        continue
      if(v[nc][nr]==0):
        v[nc][nr]=2
        q.append([nc,nr])
  # 빈칸 세기
  global result
  cnt=0
  for a in range(n):
    for b in range(m):
      if(v[a][b]==0):
        cnt+=1
  result=max(result,cnt)
  return 
    
    
def comb (cnt,prev):
  if(cnt==3):
    v=[row[:] for row in arr]
    bfs(v)
    return 
  for i in range(prev,n*m):
      if(arr[i//m][i%m]==0):
        arr[i//m][i%m]=1
        comb(cnt+1, i+1)
        arr[i//m][i%m]=0
        
comb(0,0)
print(result)