# 체커

n= int(input())
checker=[]
arr_x=[]
arr_y=[]

answer=[-1]*n

for _ in range(n):
  x,y= map(int, input().split())
  checker.append([x,y])
  arr_x.append(x)
  arr_y.append(y)
  

for x in arr_x:
  for y in arr_y:
    d=[]
    for loc in checker:
      a,b=loc
      distance= abs(a-x)+abs(b-y)
      d.append(distance)
    
    d.sort()
  
  tmp=0
  for i in range(len(d)):
    tmp+=d[i]
    if(answer[i]==-1):
      answer[i]= tmp
    else:
      answer[i]= min(answer[i],tmp)

print(*answer)