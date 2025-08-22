'''
숨바꼭질
푼날짜: 25.08.22

출력: 숨어야 하는 헛간 번호(같다면 가장 작은 번호), 헛간까지 거리, 같은 거리를 갖는 헛간 개수 
1번 헛간과 최대한 멀리 떨어지도록 

1. dps로 1번 헛간에 출발해서 각 헛간들 거리비용 계산해서 저장하기
2. 방문처리 필요!
3. 거리 계산 후 가장 작은 값이 작은 것 중 첫번째 인덱스 출력
4. 해당 값을 가진 헛간 수 구하기
'''
import sys
from collections import deque

input= sys.stdin.readline
n,m= map(int,input().split()) # 헛간의 수, m개의 간선

distance=[0]*(n+1)
barns=[[] for _ in range(n+1) ]

for _ in range(m):
  a,b= map(int,input().split())
  barns[a].append(b)
  barns[b].append(a)


q= deque()
q.append(1)
while(q):
  s=q.popleft()
  for i in barns[s]:
    if(not distance[i]):
      distance[i]= distance[s]+1
      q.append(i)

result_a=0
result_b=0
result_c=0
for k in range(2,n+1):
  if(distance[k]>result_b):
    result_b= distance[k]
    result_a= k

result_c=len(list(filter(lambda x:x==result_b, distance[2:])))

print(result_a,result_b, result_c)