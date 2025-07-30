# 수 정렬하기5
# 16% 틀림 
import sys
input= sys.stdin.readline

# 절댓값이 1_000_000 보다 작거나 같은 정수

arr=[0]*2_000_001
n= int(input())

# 0이거나 양수라면 +1_000_000해서 저장하기
for i in range(n):
  tmp= int(input())
  arr[tmp+1_000_000]+=1

for j in range(0,2_000_001):
  if(arr[j]>0):
    for _ in range(arr[j]):
      print(j-1_000_000)
  