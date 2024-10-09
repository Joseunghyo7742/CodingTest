# AC

# R은 순서를 뒤집는 함수, D는 첫 번째 수를 버리는 함수 
from collections import deque
import sys
t= int(sys.stdin.readline())

for _ in range(t):
  isError=False
  q=deque()
  p= sys.stdin.readline()
  n= int(sys.stdin.readline())
  temp=sys.stdin.readline().strip().strip("[]")
  
  if(n>0):
    line= list(map(int,temp.split(",")))
    q.extend(line)
  
  count_R= 0
  isLeft=True
  
  for i in p:
    if(i=="R"):
      isLeft= not isLeft
      count_R+=1
    elif(i=="D"):
      if(len(q)<=0):
        isError=True
        break
      elif(isLeft):
        q.popleft()
      elif(not isLeft):
        q.pop()
    
  if(isError): print("error")
  else: 
    if(count_R%2==1): q.reverse()
    print("[", ','.join(map(str,q)), "]",sep="")