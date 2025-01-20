# 수열의 길이 A와, 간격 B가 주어집니다.

# 그리고 수열이 하나 주어집니다.

# 주어진 간격만큼의 합을 구해서, 가장 큰 수를 출력하는 프로그램을 작성하세요.

# 2<=a <=100_000
# 10 3
# 3 -2 -4 -9 0 3 7 13 8 -3
# 1 -6 -13 -9 3 10 20 21 5


# 21

from collections import deque

a,b= map(int,input().split())
arr=list(map(int, input().split()))

result=-10_000_000
sum_arr=0

for i in range(b):
  sum_arr+= arr[i]
  
result= max(result,sum_arr)

for j in range(b,a):
  sum_arr-=arr[j-b]
  sum_arr+=arr[j]
  result= max(result,sum_arr)
  
print(result) 
  
  # 완탐 => 시간 초과
# result=-1
# for i in range(a-b+1):
#   tmp=0
#   for j in range(i,i+b):
#     tmp+=arr[j]
#   if(tmp>=result):
#     result=tmp
# print(result)99
    