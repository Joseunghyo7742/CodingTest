from collections import deque



def bfs(F,S,G,U,D):
  q= deque()
  q.append(S)
  build[S]=1
  move=[U,-D]
  while q:
    floor= q.popleft()
    if(floor==G):
      return build[floor]-1
    for i in range(2):
      n_floor= floor+move[i]
      if(n_floor>F or n_floor<1 or build[n_floor]!=0):
        continue
      elif(floor<G):
          build[n_floor]= build[floor]+1
          q.append(n_floor)
      elif(floor>G):
          build[n_floor]= build[floor]+1
          q.append(n_floor)
  return "use the stairs"



F,S,G,U,D= list(map(int,input().split()))
# S >F 인경우도 있다
# "use the stairs"
# u층 위, d층 아래에 해당 층이 없다면 엘베 움직이지 않는다.

build=[0 for _ in range(F+1)]
print(bfs(F,S,G,U,D))
