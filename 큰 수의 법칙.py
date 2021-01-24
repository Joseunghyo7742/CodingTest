n,m,k=map(int,input().split())
data= list(map(int,input().split())) #n개의 자연수 입력
data.sort(reverse=True)
max_1=data[0]
max_2=data[1]
result=0
if(max_1==max_2): #큰 수가 중복이 있을 경우
  result=max_1*m 
else:
  count=0 #더하는 수 카운트
  while(m!=count):
    for i in range(0,k):
      result+=max_1
      count+=1
    result+=max_2
    count+=1
print(result)