from collections import deque
n= int(input()) #경우의 수 

dx=[-2,-2,2,2,-1,-1,1,1]
dy=[-1,1,-1,1,-2,2,-2,2]

def bfs(x,y):
  if(x==e_x and y==e_y): return board[e_x][e_y] #시작점과 끝점이 같을 경우
  queue= deque()
  queue.append((x,y))
  while(queue):
    x,y= queue.popleft()
    for i in range(8):
      nx= x+dx[i]
      ny= y+dy[i]
      
      if(0<=nx<size and 0<=ny<size and board[nx][ny]==0):
          board[nx][ny]=board[x][y]+1
          queue.append((nx,ny))

  return board[e_x][e_y]
  
result=[]
while(n!=0):
  size= int(input()) #체스판 크기(4<=I<=300) I*I
  s_x, s_y= map(int,input().split()) #시작좌표
  e_x, e_y= map(int,input().split()) #끝좌표
  
  board=[[0]*size for _ in range(size)] #체스판
  board[s_x][s_y]=0
  result.append(bfs(s_x,s_y))
  
  n-=1

#결과 출력
for r in result:
  print(r)



