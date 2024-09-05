from collections import deque

n=int(input()) 
m= int(input())
net=[[] for _ in range(n+1)]

for i in range(m):
  a,b= map(int,  input().split())
  net[a].append(b)
  net[b].append(a)

def dfs(num):
  check[num] =True
  for i in net[num]:
    if(check[i]): continue
    else:
      dfs(i)
    

check=[False]*(n+1)
check[1]=True
for i in net[1]:
  dfs(i)

result= check.count(True)-1
print(result)
  
