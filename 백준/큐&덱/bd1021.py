# 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
# 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
# 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
import math
import sys
from collections import deque
n,m = list(map(int, sys.stdin.readline().split()))
want=list(map(int,sys.stdin.readline().split()))

q= deque()
for i in range(n): q.append(i+1)

result=0
for i in want:
  idx= q.index(i)
  if(idx==0):
    q.popleft()
  #오른쪽으로 돌림
  elif(idx>=math.ceil(len(q)/2)):
    temp=len(q)-idx
    q.rotate(temp)
    result+=temp
    q.popleft()
  #왼쪽으로 돌림
  else:
    temp= idx
    q.rotate(-temp)
    result+=temp
    q.popleft()
    
print(result)

