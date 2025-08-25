'''
섬의 개수 
푼날짜: 26.08.25

1은 땅 0은 바다 
가로,세로, 대각선 연결은 걸어갈 수 있다. = 섬 길
'''
import sys
from collections import deque
sys.setrecursionlimit(10**6)

input= sys.stdin.readline


direction=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
def bfs(c,r):
  q= deque()
  q.append([c,r])
  graph[c][r]=0
  
  while(q):
    cc,cr= q.popleft()
    for i in range(8):
      nc= cc+direction[i][0]
      nr= cr+direction[i][1]
      if(nc<0 or nc>=h or nr<0 or nr>=w):
        continue
      elif(graph[nc][nr]):
        graph[nc][nr]=0
        bfs(nc,nr)
  

while(True):
  w,h = map(int,input().split())
  if(w==0):
    break
  graph=[]
  for _ in range(h):
    graph.append(list(map(int,input().split())))
  
  cnt=0
  for i in range(h):
    for j in range(w):
      if(graph[i][j]):
        cnt+=1
        bfs(i,j)
  print(cnt)
