# 비내림차순 = 오름 또는 같은

def cur(i):
  if(i==m):
    print(*arr)
    return
  
  for j in range(1,n+1):
    if(i>0 and arr[-1]>j):
      continue
    arr.append(j)
    cur(i+1)
    arr.pop()
  

n,m= list(map(int,input().split()))
arr=[]
cur(0)