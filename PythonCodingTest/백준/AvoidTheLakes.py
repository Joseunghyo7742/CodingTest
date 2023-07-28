n,m,k= map(int,input().split()) #n: row, m:column k: submerged

field= [[0]*m for _ in range(n)]

for i in range(k): #1: submerged area
  r,c= map(int,input().split())
  field[r-1][c-1]=1

dx=[0,0,-1,1]
dy=[-1,1,0,0]
lake_max_size=0
size=0
def dfs(x,y):
  for i in range(4):
    nx= x+dx[i]
    ny= y+dy[i]
    if(nx<0 or ny<0 or nx>= n or ny >= m): continue
    if(field[nx][ny]==1):
      global size
      size+=1
      field[nx][ny]=2
      dfs(nx,ny)


for j in range(n):
  for u in range(m):
    if(field[j][u]==0): continue
    if(field[j][u]==1):
      dfs(j,u)
      if(size>lake_max_size): lake_max_size=size
      size=0

print(lake_max_size)