import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n= int(input())
arr=[] #건물 높이 정보 담을 배열


max_h=0#높이 최댓값
for _ in range(n):
  line= list(map(int,input().split()))
  if(max(line)>max_h): max_h= max(line)
  arr.append(line)

dx= [0,0,-1,1]
dy=[-1,1,0,0]

def dfs(x,y,h):
  for i in range(4):
    nx= x+ dx[i]
    ny= y+ dy[i]
    if(nx<0 or ny <0 or nx>=n or ny>= n): continue
    if(arr[nx][ny]>h and not visited[nx][ny]):
      visited[nx][ny]=1
      dfs(nx,ny,h)
    
result=0 #안전한 영역의 최대 개수
for k in range(max_h):
  visited= [[0]*n for _ in range(n)]
  count=0  #안전한 영역 개수
  for i in range(n):
    for j in range(n):
      if (arr[i][j]> k and not visited[i][j]): #안전 구역이 아니고 아직 방문 x
        count+=1 
        visited[i][j]=1
        dfs(i,j,k)
  result= max(result, count)
  
print(result)