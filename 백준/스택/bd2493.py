import sys

n=int(sys.stdin.readline())
height=list(map(int, sys.stdin.readline().split()))

MAX_HEIGHT= 100000001
stack=[[MAX_HEIGHT,0]]
result=[]

for i in range(n):
  #스택이 작으면 그동안 팝.
  while(stack[-1][0]<height[i]):
    stack.pop()
  result.append(stack[-1][1])
  stack.append([height[i],i+1])
  
  
print(' '.join(map(str,result)))
