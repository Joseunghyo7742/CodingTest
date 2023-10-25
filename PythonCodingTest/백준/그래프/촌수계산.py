import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n= int(input()) #전체 사람 수 
a,b= map(int,input().split()) #a,b와의 관계를 구해야 함.
m= int(input()) #관계의 개수 

graph =[[] for _ in range(n+1)]
visited=[False] *(n+1)

for _ in range(m):
  parent,child=map(int,input().split())
  graph[parent].append(child)
  graph[child].append(parent)


def dfs(x,y,rel):
  visited[x]=True
  if(y in graph[x]):
    print(rel+1)
    exit()
  else:
    for i in graph[x]:
      if(visited[i]==False):
        dfs(i,y,rel+1)
    return -1
    

result=dfs(a,b,0)
print(result)
