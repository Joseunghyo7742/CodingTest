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



# r,c,sum,tf
def bfs(r,c):
  q= deque()
  q.append([r,c,1,False])
  miro[r][c]=2
  while(q):
    r,c,s,w=q.popleft()
    if(r==n-1 and c==m-1):
      nr= dr[i]+ r
      nc= dc[i]+ c
      return s
    for i in range(4):
      if(nr<0 or nr>=n or nc<0 or nc>=m):
        continue
      if(miro[nr][nc]==0):
        miro[nr][nc]=2
        q.append([nr,nc,s+1,w])
      elif(miro[nr][nc]==1):
        if(w): continue
        else: 
          miro[nr][nc]=2
          q.append([nr,nc,s+1,not w])
      
  return -1


result= bfs(0,0)
print(result)
