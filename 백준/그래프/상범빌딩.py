from collections import deque

dx=[0,0,1,-1,0,0] 
dy=[0,0,0,0,1,-1]
dz=[-1,1,0,0,0,0]

def bfs(z,x,y,cnt):
  queue= deque()
  queue.append((z,x,y,cnt))
  
  while queue:
    z,x,y,cnt= queue.popleft()
    for i in range(6):
      nz= z+dz[i]
      nx= x+dx[i]
      ny= y+dy[i]
      
      if(0<=nz<L and 0<=nx<R and 0<=ny<C and building[nz][nx][ny]!="#"):
        if(building[nz][nx][ny]=="E"): return cnt+1
        #building[nz][nx] = building[nz][nx][:ny] + "#" + building[nz][nx][ny + 1:]
        queue.append((nz,nx,ny,cnt+1))
  return 0

while True:
  L,R,C= map(int,input().split()) #L: 빌딩 층수, R,C,: 한 층의 행과 열 수
  if L == R == C == 0 : break
  building= []

  s_z,s_x,s_y =0,0,0 #시작점의 좌표

  for i in range(L):
    floor=[]
    for j in range(R):
      line= input()
      if "S" in line: 
        s_z= i
        s_x= j
        s_y= line.index("S")
      floor.append(line)
    building.append(floor)
    input() #blank line

  result= bfs(s_z,s_x,s_y,0)
  if result==0: print("Trapped!")
  else:
    print("Escaped in %d minute(s)." %result)
          
        