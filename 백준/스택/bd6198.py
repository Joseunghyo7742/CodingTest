#옥상정원뀌기
import sys

n= int(sys.stdin.readline())

stack=[1000000000]
result=0

#추가 후 더하기
for i in range(n):
  height=int(sys.stdin.readline())
  while(stack[-1]<=height):
    stack.pop()
  result+= len(stack)-1
  stack.append(height)
  
print(result)
  
  