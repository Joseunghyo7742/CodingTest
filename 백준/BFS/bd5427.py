#불
from collections import deque

def bfs(q):
  dr=[0,0,-1,1]
  dc=[-1,1,0,0]
  day=0
  while(q):
    day+=1
    size= len(q)
    for _ in range(size):
      r,c= q.popleft()
      for i in range(4):
        nr= r+dr[i]
        nc= c+ dc[i]
        if(nr<0 or nr>=h or nc<0 or nc>=w): #범위를 벗어났다 = 탈출
          if(town[r][c]=="@"): return day
          continue
        if(town[nr][nc]=="."):
          town[nr][nc]=town[r][c]
          q.append([nr,nc])
  return "IMPOSSIBLE"

test_n= int(input())

for _ in range(test_n):
  w,h = list(map(int,input().split()))
  town=[]
  for i in range(h):
    line= list(input())
    town.append(line)
  
  q= deque()
  
  fire_loc=[]
  person=[]
  for i in range(h):
    for j in range(w):
      if(town[i][j]=="*"):
        fire_loc.append([i,j])
      elif(town[i][j]=="@"):
        person=[i,j]
  q.extend(fire_loc)
  q.append(person)
  
  print(bfs(q))
  
