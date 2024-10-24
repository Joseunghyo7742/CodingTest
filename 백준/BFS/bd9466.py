import sys 

sys.setrecursionlimit(10**6)

def dfs(n):
  global count
  visited[n]=True
  cycle.append(n)
  
  if(visited[arr[n]]==True):
    if(arr[n] in cycle):
      count-=len(cycle[cycle.index(arr[n]):])
    return
  else:
    dfs(arr[n])
    
t= int(input())
#학생 수 n
for _ in range(t):
  n= int(input())
  arr=[0]
  arr.extend(list(map(int,input().split()))) #선택된 학생 수
  visited=[False] * (n+1)
  
  count= n
  
  for i in range(1, n+1):
    if not visited[i]:
      cycle=[]
      dfs(i)
    
    
