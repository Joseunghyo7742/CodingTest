# 중복금지, 수열은 사전 순으로 증가하는 순서 출력
# N개의 자연수 중 m개를 고른 수열 
def cur(i):
  if(i==m):
    print(*arr)
    return
  for j in range(0,n):
    if(visited[j]):
      continue
    arr.append(n_arr[j])
    visited[j]=1
    cur(i+1)
    arr.pop()
    visited[j]=0

  

n,m= list(map(int, input().split()))
n_arr=list(map(int,input().split()))
n_arr.sort()
# 1 7 9 8 


visited=[0 for _ in range(n)]
arr=[]
cur(0)