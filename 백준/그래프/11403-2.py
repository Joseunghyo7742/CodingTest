'''
경로 찾기 복습
푼날짜: 25.08.18
가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 
'''

n= int(input())
adj=[]
for _ in range(n):
  adj.append(list(map(int,input().split())))
  
def dfs(s):
  for k in range(n):
    if(adj[s][k] and not visited[k]):
      visited[k]=1
      dfs(k)

for i in range(len(adj)):
  visited=[0]*n
  dfs(i)
  print(*visited)