# n개 내림차순
# n은 1_000_000까지

import sys
input= sys.stdin.readline

n= int(input())
arr=[]
for _ in range(n):
  arr.append(int(input()))

arr.sort(reverse=True)

for i in arr:
  print(i)