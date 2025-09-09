'''
n과 m

N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
사전 순 증가
'''

n,m= map(int,input().split())
arr=list(map(int,input().split()))

arr.sort()

tmp=[]
# s원소부터 시작해서 쭉 넣어본것 
def dfs(s):
  if len(tmp)==m:
    print(*tmp)
    return
  for i in range(s, len(arr)):
    tmp.append(arr[i])
    dfs(0)
    tmp.pop()
dfs(0)
