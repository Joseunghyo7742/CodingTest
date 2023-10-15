import sys
sys.setrecursionlimit(10**6) #재귀호출 제한을 늘림
input= sys.stdin.readline
#정점의 개수 N, 간선의 개수 M
n,m = map(int,input().split())
arr= [[0]*n for _ in range(n)]

for i in range(m):
  u,v= map(int,input().split())
  arr[u-1][v-1]=1
  arr[v-1][u-1]=1
  

check=[False]*n;
count=0

def dfs(i):
  for j in range(n):
    if arr[i][j]==1 and not check[j]:
      check[j]=True
      dfs(j)
for i in range(n):
  if not check[i]:
    count+=1
    count[i]=True
    dfs(i)
print(count)