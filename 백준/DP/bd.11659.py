n,m= list(map(int,input().split()))
num=list(map(int,input().split()))

temp=0
d=[0]
for j in num:
  temp= temp+j
  d.append(temp)

for i in range(m):
  i,j= list(map(int,input().split()))
  print(d[j]-d[i-1])
  