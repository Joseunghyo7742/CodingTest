# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

def recur(i):
  if i==m:
    print(*arr)
    return
  for j in range(1,n+1):
    if(visited[j]):
      continue
    if(i>=1 and j<arr[i-1]): # 오름차순 및 중복제거 
      continue
    visited[j]=1
    arr.append(j)
    recur(i+1)
    arr.pop()
    visited[j]=0
    
    

arr=[] # 큐 같은 역할 
n,m = list(map(int,input().split()))
visited=[0 for _ in range(n+1) ]

recur(0)