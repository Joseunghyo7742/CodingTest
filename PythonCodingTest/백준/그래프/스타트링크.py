from collections import deque
F, S, G, U, D= map(int,input().split()) #총 F층, 현위치 S층, 목표 G층, 위로 U층씩 올라감, 아래로 D층씩 내려감

check=[0]*F
queue=deque()
result=0

if(S==G): 
  print(0) 
  exit()

queue.append((S,0))

while(queue):
  x,cnt= queue.popleft()
  if(x==G):
    result= cnt
    break
  up= x+U
  down= x-D
  if(up<=F and check[up-1]==0):
    check[up-1]=1
    queue.append((up,cnt+1))
  if(down>0 and check[down-1]==0):
    check[down-1]=1
    queue.append((down,cnt+1))


if(result==0): print("use the stairs")
else: print(result)