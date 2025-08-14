'''
BFS와 DFS
푼 날짜: 25.08.12
출력: DFS 결과 , BFS 결과
'''
from collections import deque
import sys 


def dfs(s):
  dfs_route.append(s)
  visited[s]=1
  for k in sorted(graph[s]):
    if(not visited[k]):
      dfs(k)

def bfs(s):
  q= deque()
  q.append(s)
  visited[s]=1
  bfs_route.append(s)
  
  while(q):
    curr=q.popleft()
    bfs_route.append(curr)
    for k in sorted(graph[curr]):
      if(not visited[k]):
        visited[k]=1
        q.append(k)
  
    
  
input= sys.stdin.readline
n,m,v= map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(n):
  a,b= map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

visited=[0]*(n+1)
dfs_route=[]
bfs_route=[]

dfs(v)
visited=[0]*(n+1)
bfs(v)

print(*dfs_route)
print(*bfs_route)

