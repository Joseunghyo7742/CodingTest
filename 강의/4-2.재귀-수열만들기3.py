# 같은 수를 여러 개 골라도 된다.

def curr(i):
  if(i==m):
    print(*arr)
    return
  for j in range(1,n+1):
    arr.append(j)
    curr(i+1)
    arr.pop()

n,m = list(map(int,input().split()))
arr=[] # 만들어진 수열

curr(0)
