
n,s= map(int,input().split()) #n:정수의 개수, s:목표 정수
arr= list(map(int,input().split())) #부분수열 목록
cnt=0

def dfs(i,sum):
  global cnt
  if i >=n:
    return
  sum+= arr[i]
  if sum==s:
    cnt+=1
  
  dfs(i+1, sum)
  dfs(i+1, sum-arr[i])

dfs(0,0)
print(cnt)