n,m= map(int,input().split())
result=0
for i in range(n):
  data= list(map(int,input().split()))
  min_value= min(data)
  result=max(result, min_value)
print(result)

"""
n,m= map(int,input().split())
result=0

for i in range(n):
  data= list(map(int,input().split()))
  min_value=1001
  for a in data:
    if(a<min_value):
      min_value=a
  result=max(result, min_value)
    
"""