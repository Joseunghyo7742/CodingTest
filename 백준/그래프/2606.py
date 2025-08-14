'''
바이러스
푼 날짜: 25.08.12

바이러스 걸린 컴퓨터 대 수 구하기
'''
import sys
from collections import deque
input = sys.stdin.readline


n= int(input())
v= int(input())

cnnt=[[] for _ in range(n+1)]
for _ in range(v):
  a,b= map(int,input().split())
  cnnt[a].append(b)
  cnnt[b].append(a)

checked=[0]*(n+1)

cnt=0
q= deque()
q.append(1)
checked[1]=1

while(q):
  curr= q.popleft()
  for k in cnnt[curr]:
    if(not checked[k]):
      checked[k]=1
      cnt+=1
      q.append(k)

print(cnt)