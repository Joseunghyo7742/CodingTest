# 세 수의 합
# U 원소 중 세 개의 합이 U에 포함된 경우, 가장 큰 합

# 삼중포문보다 이중포문이 낫다는것!

n= int(input())
U=set() # U원소는 200_000_000이하 자연수 
      
for _ in range(n):
  U.add(int(input()))

sums= set() # 두 수의 합 - 중복조합 
for i in U:
  for j in U:
    sums.add(i+j)


result=-1
# 탐색하기 
for k in U:
  for r in U:
    if(k-r in sums):
      result= max(result, k)

print(result)