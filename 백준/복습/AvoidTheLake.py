import sys
sys.setrecursionlimit(10**6) #재귀호출 제한을 늘림
input= sys.stdin.readline

n,m,k= map(int,input().split())

farm= [[0]*m for _ in range(n)]

#submerged된 곳 1
for _ in range(k):
  c,r= map(int,input().split())
  farm[c-1][r-1]=1

d_c= [-1,1,0,0]
d_r=[0,0,-1,1]

result=0 #제일 넓은 lake의 넓이
count=1 #lake만날 때 카운트 시작

def dfs(c,r):
  global count
#이미 방문한 submerged지역은  0으로 변경
  farm[c][r]=0 
  for i in range(4):
    new_c= c+ d_c[i]
    new_r= r+ d_r[i]
    if(new_c<0 or new_c>=n or new_r<0 or new_r>=m):
      continue
    if(farm[new_c][new_r]==1):
      count+=1
      dfs(new_c,new_r)

for i in range(n):
  for j in range(m):
    if(farm[i][j]==1):
      dfs(i,j)
      if(count>result):
        result=count
      count=1

print(result)

