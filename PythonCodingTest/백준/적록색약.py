import sys
sys.setrecursionlimit(10 ** 6)


n= int(input())
pic= []
for _ in range(n):
  pic.append(list(input()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

switch = 1
def dfs(x,y):
  visited[x][y]=switch
  color= pic[x][y]
  for i in range(4):
    nx= x+dx[i]
    ny= y+dy[i]
    if(nx<0 or ny<0 or nx>=n or ny>=n or visited[nx][ny]== (switch)): continue
    if( pic[nx][ny]==color):
      visited[nx][ny]=switch #적록색약일때 0
      dfs(nx,ny)
  
    
visited=[[0]*n for _ in range(n)]
a=0 #적록색약 아닌 사람
tmp=0

for c in range(2):
  for i in range(n):
    for j in range(n):
      if(visited[i][j]!=switch):
        dfs(i,j)
        tmp+=1
        
  if(c==0): 
    a=tmp
    tmp=0
    for i in range(n):
      for j in range(n):
        if(pic[i][j]=="G"):
          pic[i][j]="R"
  switch=0

print(a,tmp)