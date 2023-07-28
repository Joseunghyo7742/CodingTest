r,c,k= map(int,input().split()) #r*c 크기 맵,k:거리
field=[list(input()) for _ in range(r)]
visited=[[0]*c for _ in range(r)] #방문체크
result=0

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,cnt):
  global result
  visited[x][y]=1
  if [x,y] ==[0,c-1] and cnt==k:
    result+=1
    return
  for i in range(4):
    nx= x+ dx[i]
    ny= y+ dy[i]
    if(0<= nx < r and 0<= ny < c and visited[nx][ny]==0 and field[nx][ny]!='T'):
        visited[nx][ny]=1
        dfs(nx,ny,cnt+1)
        visited[nx][ny]=0
        

dfs(r-1,0,1)
print(result)
