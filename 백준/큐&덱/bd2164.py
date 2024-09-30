from collections import deque


q= deque()

n= int(input())
for i in range(n):
  q.append(i+1)

while(len(q)>1):
  q.popleft()
  if(len(q)>1):
    q.append(q.popleft())

print(q[0])
  

  