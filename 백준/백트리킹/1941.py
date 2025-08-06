# 소문난 칠공주
# S학생 적어도 4명 이상 
# 7명, 서로 인접

# 몇개의 경우가 있는지 만들어보기
# 백트래킹으로 모든 조합을 만들어보고, y가 4개이상이 되면 만들기 그만!! 

from collections import deque as dq

seats=[]

for _ in range(5):
  seats.append(input())

res=0 #결과 저장
arr=[] #조합
direction=[(0,1),(0,-1),(1,0),(-1,0)]

# 이어지는지 확인하는 함수
def bfs(comb):
  visit=[[1]*5 for _ in range(5)] #방문 여부 확인
  for i in comb:
    x,y= i
    visit[x][y]=0 #선택된 7명을 0으로 표시
  
  cnt_tmp =1 # 인접한 학생 수 카운트
  q= dq([comb[0]]) # 시작점
  visit[comb[0][0]][comb[0][1]] = 1
  while(q):
    x,y= q.popleft()
    for dx,dy in direction:
      nx, ny = x+dx, y+dy
      if nx in range(5) and ny in range(5): #격자 범위 안인지 확인
        if not visit[nx][ny]:
          visit[nx][ny]
          cnt_tmp+=1
          q.append((nx,ny))
  if cnt_tmp!=7:
    return False
  else:
    return True 
    
  

# 백트래킹으로 조합을 생각하자
def combi(length=0, start=0, cnt=0): # cnt-임도연파 학생
  global res
  if cnt>= 4:
    return

  if length == 7:
    if(bfs(arr)):
      res+=1
    return
  for i in range(start,25):
    x,y= i//5, i%5 #x는 행, y는 열 
    arr.append((x,y))
    combi(length+1, i+1, cnt+(seats[x][y]=='Y'))
    arr.pop()
  
combi()
print(res)