n= int(input())
location=[]
arr_x=[]
arr_y=[]
answer=[-1]*n
for _ in range(n):
  x,y= map(int,input().split())
  arr_x.append(x)
  arr_y.append(y)
  location.append([x,y])

for y in arr_y:
  for x in arr_x:
    dist=[]
    for ex,ey in arr:
      d= abs(ex-x)+ abs(ey-y)
      dist.append(d)
      
    dist.sort() #가까운 순으로 정렬
    temp=0
    for i in range(len(dist)):
      d= dist[i]
      temp+=d
      if answer[i]==-1:
        answer[i]=temp
      else:
        answer[i]= min(temp, answer[i])
print(*answer)

