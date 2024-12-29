#0 이동 가능, 1벽
#벽 한 개까지 부수고 이동 가능. 
# 불가 -1


from collections import deque

n,m= list(map(int,input().split()))
miro=[]
for _ in range(n):
  miro.append(list(map(int,input())))

dr=[0,0,-1,1]
dc=[1,-1,0,0]

#3차원배열 move[c][r][break] 
move=[[[0,0] for _ in range(m)] for _ in range(n)]

print(move)
def bfs(r,c):
  q= deque()
  q.append([r,c,0])
  move[r][c][0]=1
  while(q):
    r,c,count=q.popleft()
    if(r,c)==(n-1,m-1):
      return move[r][c][count]
    for i in range(4):
      nr= dr[i]+ r
      nc= dc[i]+ c
      if(nr<0 or nr>=n or nc<0 or nc>=m):
        continue
      #벽인 경우 부순다. 
      if(miro[nr][nc]==1 and count==0):
        move[nr][nc][1] = move[r][c][0]+1 
        q.append([nr,nc,1])
      #이동 가능, 아직 방문하지 않은 곳 
      if(miro[nr][nc]==0 and move[nr][nc][count]==0):
        move[nr][nc][count] = move[r][c][count]+1 
        q.append([nr,nc,count])
  return -1

print(bfs(0,0))
