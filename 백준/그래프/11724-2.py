'''
연결 요소의 개수
푼 날짜: 25/8/11

입력: 정점의 개수 n, 간선의 개수 m 
출력: 연결 요소의 개수 
'''
from collections import deque
import sys

n,m= map(int,input().split())
input= sys.stdin.readline

# 인접리스트 방식
graph=[[] for _ in range(n+1)]

for _ in range(m):
  u,v= map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)

cnt=0
visited=[0]*(n+1)

def bfs(s):
  q=deque()
  visited[s]=1
  q.append(s)
  while(q):
    curr= q.popleft()
    for k in graph[curr]:
      if(not visited[k]):
        visited[k]=1
        q.append(k)

        
for i in range(1,n+1):
  if(not visited[i]):
    cnt+=1
    bfs(i)
print(cnt)  
