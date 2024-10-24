# 팀원을 만드는 사이클 찾기
# 사이클이 만들어지는 사람들 임시저장 
# 팀이 만들어진다면, 임시저장만큼 인원수빼기
# 중복해서 뺴면안되니까, 방문을 체크하기.
import sys
sys.setrecursionlimit(10**6)
t= int(input())

def dfs(n):
  global cnt
  visited[n]= True
  temp.append(n)
  
  if(visited[arr[n]]==True):
    if(arr[n] in temp):
      cnt-=len(temp[temp.index(arr[n]):]) 
    return
  else:
    dfs(arr[n])

for _ in range(t):
  n= int(input())
  arr=[0]
  arr.extend(list(map(int,input().split())))
  cnt=n
  visited =[False for _ in range(n+1)]
  
  for i in range (1,n+1):
    if(not visited[i]):
      temp=[]
      dfs(i)

  print(cnt)
