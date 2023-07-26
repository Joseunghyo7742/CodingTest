
n,s= map(int,input().split()) #n:정수의 개수, s:목표 정수
arr= list(map(int,input().split())) #부분수열 목록
cnt=0

def dfs(num,sum):
  global cnt
  if num >=n:
    return
  sum+= arr[num]
  if sum==s:
    cnt+=1
  
  dfs(num+1, sum)
  dfs(num+1, sum-arr[num])

dfs(0,0)
print(cnt)