import sys
sys.setrecursionlimit(1000000)
n,m = map(int, input().split())
pic=[]
for i in range(n):
  pic.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]


sum=1
def dfs(y,x):
  for i in range(4):
    ny= y+dy[i]
    nx= x+dx[i]
    if ny<0 or ny>=n or nx<0 or nx>=m:
      continue
    if pic[ny][nx]==1:
      pic[ny][nx]= 0
      global sum
      sum+=1
      dfs(ny,nx)

cnt=0
max_val=0

for i in range(n):
  for j in range(m):
    if(pic[i][j]==1):
      pic[i][j]=0
      dfs(i,j)
      max_val=max(max_val,sum)
      sum=1
      cnt+=1
      
# print(pic)
# max_val= max(map(max, pic))
print(cnt,max_val,sep='\n')