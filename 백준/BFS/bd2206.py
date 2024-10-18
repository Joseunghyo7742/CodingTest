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

def bfs(r,c):
  q= deque()
  q.append([r,c])
  miro[r][c]=2
  count=1
  while(q):
    r,c=q.popleft()
    for i in range(4):
      nr= dr[i]+ r
      nc= dc[i]+ c
      if(nr<0 or nr>=r or nc<0 or nc>=c):
        continue
      if(miro[nr][nc]==0):
        miro[nr][nc]=2
        count+=1
        q.append([nr,nc])
        print(q)
  
  if(miro[n-1][m-1]==2): return -1
  else: return count


result= bfs(0,0)
print(result,miro)