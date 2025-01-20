a,b,c,d,e,f= list(map(int,input().split()))
for x in range(-10_000,10_001):
  for y in range(-10_000,10_001):
    if(a*x + b*y ==c):
      if(d*x + e*y ==f):
        print(x,y)
        break