# n개의 빌딩, h 빌딩들의 높이 
# i번째 빌딩 관리인이 볼 수 있는 다른 빌딩 옥상 정원은 i+1, i+2, ...,n
# 더 높거나 같으면  빌딩부터 다음 빌딩들 다 못봄
# 관리인들이 볼 수 있는 빌딩 수의 합

n= int(input())
stack=[-1]


cnt=0
for _ in range(n):
  top= stack[-1]
  k= int(input())
  
  # 스택에 맨 위 > k 스택 길이만큼 더함, 스택에 k쌓기 
  if(top>k):
    cnt+= len(stack)-1
    stack.append(k)
    
  # 스택 맨위 <=k  k보다 큰값 나올 때까지 스택에서 빼기
  else:
    while(len(stack)>1 and stack[-1]<=k):
      stack.pop()
    cnt+= len(stack)-1
    stack.append(k)
print(cnt)



