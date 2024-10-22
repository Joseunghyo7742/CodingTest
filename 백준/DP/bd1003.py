
t= int(input())


fibo=[[1,0],[0,1]]

for i in range(2,41):
  a,b= fibo[i-1]
  c,d= fibo[i-2]
  fibo.append([a+c,b+d])


for _ in range(t):
  num= int(input())
  print(' '.join(map(str,fibo[num])))