# 왼 -> 오 
# 가장 먼저 만나는 단 하나의 탑에서만 수신 가능
# 각각 탑에서 발사한게 어느 탑에서 수신하는지
# 수신하는 탑이 없다면 0
# 6 9 5 7 4
# 0 0 

# 스택에 쌓인것보다 큰 수라면 , 큰 수를 만날때까지 pop하고 넣기
# 스택에 쌓인 것보다 작은 수면 그냥 넣기
# 이때 큰 수를 만나면 그 스택의 인덱스를 result에 넣는다. 

t=[100000001]

n= int(input())
tops= list(map(int,input().split()))
t.extend(tops)

result=[0]
stack=[[0,t[0]]] # 인덱스, 탑높이

for i in range(1,n+1):
  while(stack[-1][1]<= t[i]):
    stack.pop()
  result.append(stack[-1][0])
  stack.append([i,t[i]])


print(*result)