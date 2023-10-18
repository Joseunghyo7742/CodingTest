from collections import deque

m,n= map(int,input().split())
d= [(0,-1),(0,1),(1,0),(-1,0)]
box=[]

for _ in range(n):
  box.append(list(map(int,input().split())))

queue=deque()

for i in range(n):
  for j in range(m):
    if box[i][j]==1:
      queue.append((i,j,0))
      
while queue:
  c,r,day = queue.popleft()
  # for i in range(n):
  #   print(box[i])
  # print("*********")
      
  for dc,dr in d:
    new_c= c+dc
    new_r= r+dr
    if(new_c <0 or new_c>=n or new_r<0 or new_r>=m):
      continue
    if(box[new_c][new_r]!=0 ):
      continue
    box[new_c][new_r]=day+1
    queue.append((new_c,new_r,day+1))
      
max_day=1
for i in range(n):
  for j in range(m):
    if box[i][j]==0:
      print(-1)
      exit()
    if box[i][j]>max_day:
      max_day= box[i][j]


result=0
for i in box:
  if 0 in i:
    result=-1
    break
  result= max(max(i)-1,result) #위에 bfs에서 날짜 카운트시 하루지났을 때 2일차로 치기때문
print(result)