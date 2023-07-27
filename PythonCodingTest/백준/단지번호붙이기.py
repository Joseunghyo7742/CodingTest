import sys
sys.setrecursionlimit(10 ** 6)

n= int(input())
arr= []
dx=[0,0,-1,1]
dy=[-1,1,0,0]
dangi= []
size=1

for i in range(n):
  arr.append(list(map(int,input())))
  
def dfs(x,y):
  global size;
  for k in range(4):
    nx= x+dx[k]
    ny= y+dy[k]
    if(nx<0 or ny<0 or nx>=n or ny>= n): continue
    if(arr[nx][ny]==1):
      size+=1
      arr[nx][ny]=2 #들어간 집 체크
      dfs(nx,ny)

for i in range(n):
  for j in range(n):
    if(arr[i][j]==1):
      arr[i][j]=2 #방문한 것으로 체크
      dfs(i,j)
      dangi.append(size) #단지 내 집 수 배열에 추가
      size=1 #사이즈 초기화
      
dangi.sort()
print(len(dangi))
for k in dangi:
  print(k)