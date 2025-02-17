def cur(i):
  if(i==m):
    print(*arr)
    return
  for j in range(n):
    if(v[j]):
      continue
    if(i>0 and arr[-1]>=n_arr[j]):
      continue
    arr.append(n_arr[j])
    v[j]=1
    cur(i+1)
    v[j]=0
    arr.pop()
    
  
  
n,m= list(map(int, input().split()))
n_arr= list(map(int, input().split()))
n_arr.sort()
v=[0 for _ in range(n)]
arr=[]

cur(0)