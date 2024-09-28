import sys

n= int(sys.stdin.readline())
top= list(map(int, sys.stdin.readline().split()))

stack=[[top[0],1]] #2차원 리스트로 [탑 높이, 탑 번호]

result=[0] #초기는 왼쪽으로 레이저가 가기때문에 무조건 0이다

if(n==1):
  print(result[0])
  exit()

for i in range(1,n):
  #top값이 스택 맨 위 값보다 작거나 같을 때,
  if(stack[-1][0] >= top[i]): 
    result.append(stack[-1][1])
    
  #top값이 스택 맨 위보다 더 클 때 
  else: 
    check=False
    #스택을 돌며 더 높은 값이 있나 확인 
    while(len(stack)>0):
      if(stack[-1][0]>=top[i]):
        result.append(stack[-1][1])
        check=True
        break
      stack.pop()
    if(not check):result.append(0)  
  stack.append((top[i],i+1))
  
print(' '.join(map(str, result)))
      
      

# 5
# 6 9 5 7 4

# 0 0 2 2 4 

