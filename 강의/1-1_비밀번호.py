n= int(input())

for _ in range(n):
  pw = int(input())
  for j in range(2,1_000_001):
    if(pw%j==0):
      print("NO")
      break
    if(j==1_000_000):
      print("YES")
  