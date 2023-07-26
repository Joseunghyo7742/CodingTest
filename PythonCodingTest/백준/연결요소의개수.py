import sys
sys.setrecursionlimit(10**6) #재귀호출 제한을 늘림
input= sys.stdin.readlinen

n,m= map(int,input().split())
arr= [[0]*n for _ in range(n)] #n*n행렬

for i in range(m): #간선의 양 끝점 인접행렬에 표시 
  u,v= map(int,input().split()) 
  arr[u-1][v-1]= 1
  arr[v-1][u-1]=1
  
chk=[False]*n #방문한 노드 체크 
cnt=0

def dfs(i): #깊이 우선 탐색으로 연결 요소를 모두 방문
  for j in range(n):
    if arr[i][j]==1 and not chk[j]:
      chk[j]=True
      dfs(j)

for i in range(n):
  if not chk[i]:
    cnt+=1
    chk[i]=True
    dfs(i)
print(cnt)