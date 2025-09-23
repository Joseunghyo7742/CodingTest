'''
아기상어
푼날짜: 25.09.17

0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치

몇 초 동안 물고기를 잡아먹을 수 있느냐?

1. 아기상어 크기만큼 물고기를 잡아먹으면 크기+1
2. 자신보다 큰 물고기는 벽
3. 먹을 수 있는 물고기 1마리면 먹으러감. 여러마리면 가장 가까운 물고기부터 

처음 아기상어 크기는 2
크기가 작은물고기만 먹을 수 있음
물고기 먹은 칸은 0으로 변경 

'''
from collections import deque

direct=[(-1,0),(0,-1),(1,0),(0,1)]

def bfs(c,r):
  global time,size,s_cnt
  dist = [[-1]*n for _ in range(n)]
  dq = deque()
  dq.append((c, r))
  dist[c][r] = 0

  while dq:
    cc,cr=dq.popleft()
    for dc, dr in direct:
      nc, nr = cc + dc, cr + dr
      if nc < 0 or nc >= n or nr < 0 or nr >= n: 
        continue
      if dist[nc][nr] != -1: # 방문한 곳 스킵
        continue
      if m[nc][nr] > size: 
        continue
      dist[nc][nr] = dist[cc][cr] + 1 #0이거나 먹을 수 있는 물고기크기라면 거리 저장 
      dq.append((nc, nr))  
  # 먹을 수 있는 물고기 중 최단거리 고르기
  best= None # 거리, 행, 열
  for i in range(n):
    for j in range(n):
      if m[i][j]!=0 and m[i][j] <size and dist[i][j]!= -1:
        cand= (dist[i][j],i,j)
        if best is None or cand <best:
            best=cand
            
  if best is None:
    return 0  # 더 못 먹음
  else:
    d, i, j = best
    return (i, j, d)


n= int(input())  # 공간의 크기 nxn
m=[list(map(int,input().split())) for _ in range(n)]

# start 찾기
for i in range(n):
  for j in range(n):
    if m[i][j] == 9:
      sc, sr = i, j
      m[i][j] = 0   # 시작 칸도 빈칸으로
      break
size = 2
s_cnt = 0
time = 0

while True:
  res = bfs(sc, sr)
  if res == 0: 
    break
  nc, nr, d = res
  time += d # 이동 시간 누적
  s_cnt += 1
  if s_cnt == size:  # 성장 체크
    size += 1
    s_cnt = 0
  m[nc][nr] = 0   # 먹은 칸은 빈칸
  sc, sr = nc, nr # 상어 위치 갱신

print(time)
      


