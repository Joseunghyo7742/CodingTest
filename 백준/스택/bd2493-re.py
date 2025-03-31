# 왼 -> 오 
# 가장 먼저 만나는 단 하나의 탑에서만 수신 가능
# 각각 탑에서 발사한게 어느 탑에서 수신하는지
# 수신하는 탑이 없다면 0
# 6 9 5 7 4
n= int(input())
tops= list(map(int,input().split()))
result=[]
stack=[tops[0]]
for i in range(1,n):
  # 스택에 쌓이 값보다 크다면, result에 스택값을 넣어준다.
  if(stack[-1]>= tops[i]):
    result.append(stack.pop())
    stack.append(i)
  else:
    
  