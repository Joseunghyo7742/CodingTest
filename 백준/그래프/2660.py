'''
회장뽑기
푼날짜: 25.08.18

출력: 회장 점수와 회장이 될 수 있는 모든 사람 회장은 점수가 가장 낮은 사람이 됨 

예를 들어 어느 회원이 다른 모든 회원과 친구이면, 이 회원의 점수는 1점이다. = 해당 배열에 다른 번호가 다 있다면
어느 회원의 점수가 2점이면, 다른 모든 회원이 친구이거나 친구의 친구임을 말한다. = 다른 번호가 있거나, 한번 건너 친구로 다 넣어진다면
또한 어느 회원의 점수가 3점이면, 다른 모든 회원이 친구이거나, 친구의 친구이거나, 친구의 친구의 친구임을 말한 = 두번건너 친구 
'''

from collections import deque
import sys

input= sys.stdin.readline

n= int(input()) # 회원 수 
fr=[ [] for _ in range(n+1)]
while(True):
  a,b= map(int,input().split())
  if(a==-1):
    break
  fr[a].append(b)
  fr[b].append(a)


# 각 노드 별로 돌아보기, 몇 번에 걸쳐 방문한건지 기록하기 
visited=[0]*(n+1)

def bfs(s):
  q= deque()
  q.append([s,1])
  visited[s]=1
  while(q):
    curr,dept=q.popleft()
    
    for k in fr[curr]:
      if(not visited[k]): # 아직 방문하지 않았다면
        visited[k]=dept
        q.append([k,dept+1])

score=[99999]*(n+1) # 인맥 점수 
for i in range(1,n+1):
  bfs(i)
  score[i]=max(visited)
  visited=[0]*(n+1) #방문 초기화하기


# 회장 후보의 점수와 후보의 수를 출력하고, 두 번째 줄에는 회장 후보를 오름차순으로 모두 출력
min_score= min(score)
candidates= list(filter(lambda x: score[x]==min_score, range(len(score))))

print(min_score,len(candidates))
print(*candidates)
