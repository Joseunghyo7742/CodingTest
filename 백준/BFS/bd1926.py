from collections import deque


n,m = list(map(int, input().split()))

draw=[]
for i in range(n):
  line= list(map(int,input().split()))
  draw.append(line)


dc=[0,1,0,-1]
dr=[1,0,-1,0]

def bfs(c,r):
  q= deque()
  q.append([c,r])
  count=1
  while (q):
    c,r=q.popleft()
    for i in range(4):
      nc= c+dc[i]
      nr= r+dr[i]
      if(nc<0 or nc>=n or nr<0 or nr>=m):
        continue
      elif(draw[nc][nr]==1):
        draw[nc][nr]= 0
        count+=1
        q.append([nc,nr])
  return count


value=0
count=0
for i in range(n):
  for j in range(m):
    if(draw[i][j]==1):
      draw[i][j]=0
      value= max(bfs(i,j),value)
      count+=1
      
print(count)
print(value)
# max_value= max(list(map(max, draw)))
# print(draw)
# print(max_value)
          
          
    