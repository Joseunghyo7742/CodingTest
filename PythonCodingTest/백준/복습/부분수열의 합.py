import sys
sys.setrecursionlimit(10**6) #재귀호출 제한을 늘림
input= sys.stdin.readline
n,s = map(int,input().split())
arr= list(map(int,input().split()))

result=0

def dfs(sum, index):
  global result

  if(index==n):
    return
  new_sum= sum+ arr[index]
  if(new_sum==s):
    result+=1
  
  dfs(sum, index+1)
  dfs(new_sum, index+1)
  #   dfs(sum, ++index)
  # dfs(new_sum, ++index) 파이썬 증감연산자 없음!!
dfs(0,0)
print(result)