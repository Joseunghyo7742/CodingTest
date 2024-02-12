a,b= map(int,input().split())

result=1
while(a!=b and b>a):
  if(b%2==0):
      b=b//2
      result+=1
  elif(b>=11 and b%10==1):
    b= (b-1)//10
    
    result+=1

  else: break
    
if(b!=a): result=-1
print(result)