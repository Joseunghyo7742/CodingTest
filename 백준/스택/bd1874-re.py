# 스택에 푸시하는 순서는 오름차순
# 푸시는 + 팝은 -
# 입력: n, 수열 1-n이하 숫자 
# 4,3,6,8,7,5,2,1

# 해당 수를 만날때까지 push
# 스택에 있다면 pop
# 스택에 없다면 또 해당 수까지 push

# 현재 수열 값이 스택에서 pop할 값보다 작은 경우 NO 

import sys 
n= int(sys.stdin.readline())

result=[]
stack=[]
s=1

for i in range(n):
  num= int(input())
  while(s<=num):
    stack.append(s)
    result.append('+')
    s+=1
  if(stack[-1]==num):
    stack.pop()
    result.append('-')
  else:
    print("NO")
    exit
    
for r in result:
  print(r)