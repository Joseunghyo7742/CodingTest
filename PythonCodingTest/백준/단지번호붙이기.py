import sys
sys.setrecursionlimit(10 ** 6)

n= int(input())
arr= []
dx=[0,0,-1,1] #방향 설정
dy=[-1,1,0,0]
dangi= [] #단지 내 집 개수 담아줄 배열
cnt=1 #단지 내 집 수 카운트

for i in range(n):
  arr.append(list(map(int,input()))) 
  
def dfs(x,y):
  global size;
  for k in range(4): #동서남북 확인
    nx= x+dx[k]
    ny= y+dy[k]
    if(nx<0 or ny<0 or nx>=n or ny>= n): continue #범위를 벗어난 경우
    if(arr[nx][ny]==1): #집이 있는 경우우
      cnt+=1 #집 개수 카운트
      arr[nx][ny]=2 #카운트한 집은 2로 바꿔준다
      dfs(nx,ny)

for i in range(n):
  for j in range(n):
    if(arr[i][j]==1):
      arr[i][j]=2 #카운트한 집으로 체크
      dfs(i,j)
      dangi.append(cnt) #단지 내 집 수 배열에 추가
      cnt=1 #집 개수 초기화
      
dangi.sort() #오름차순 정렬
print(len(dangi)) #단지 개수 출력
for k in dangi:
  print(k)