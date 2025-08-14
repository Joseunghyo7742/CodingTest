'''
연결 요소의 개수
푼 날짜: 25/8/11

입력: 정점의 개수 n, 간선의 개수 m 
출력: 연결 요소의 개수 
'''
import sys
sys.setrecursionlimit(100000)

input= sys.stdin.readline
n,m= map(int,input().split())

# 인접행렬 방식
graph=[[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)

for _ in range(m):
  u,v= map(int,input().split())
  graph[u][v]=1
  graph[v][u]=1


def dfs(node):
  visited[node]=1
  for i in range(1,n+1):
    if(graph[node][i]==1 and not visited[i]):
        dfs(i)

result=0
for i in range(1,n+1):
  if(not visited[i]):
    dfs(i)
    result+=1
    
print(result) 
        
      