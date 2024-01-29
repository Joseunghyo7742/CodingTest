n= int(input())
curr= list(map(int,input()))
want= list(map(int,input()))

def minSwitch(cc,w,result):
  c= list(cc) #배열 복사본 생성해야함. 
  press=result
  for i in range(1,n):
    if(c[i-1]!=w[i-1]):
      press+=1
      c[i-1]=1-c[i-1]
      c[i]=1-c[i]
      if(i+1<n):
        c[i+1]=1-c[i+1]
  if(c!=w): press=9999999
  return press

#첫 번째 스위치를 안누를경우
result1= minSwitch(curr,want,0)
#두 번째 스위치를 누를 경우
curr[0]=1-curr[0]
curr[1]=1-curr[1]
result2= minSwitch(curr, want,1)

res= min(result1,result2)
if(res==9999999):
  res=-1
print(res)
  


