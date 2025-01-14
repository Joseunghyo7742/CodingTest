n= int(input()) # 1<=n <=100_000
arr= list(map(int, input().split()))



# 연속된 수 1개 이상 , 최대값

# 더하고, 이전 값 뺀 것과 비교

answer=0
for i in range(n):
  if(i==0):
    answer+=arr[i]
  else:
    if(arr[i]>answer):
      tmp= arr[i-1]+arr[i]
    
      
    tmp= answer+ arr[i]
    if(tmp<answer):
      continue
    elif(tmp> arr[i]):
      answer=tmp
    elif(tmp<arr[i]):
      answer= arr[i]

print(candy,answer)
print(max(candy))
      
    
    
