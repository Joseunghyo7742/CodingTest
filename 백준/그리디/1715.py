'''
카드 정렬하기

푼 날짜: 25.09.15

A 묵음 B묶음 비교횟수는 A+B
10 20 40 
a  b  c

n<=100000
최소한의 몇 번 비교가 필요한지 구하기 


'''

import sys, heapq

input= sys.stdin.readline
n= int(input())
hq=[]
for _ in range(n):
  heapq.heappush(hq, int(input()))
  
  
ans=0
if n<=1:
  print(0)
  sys.exit(0)
while(len(hq)>1):
  a= heapq.heappop(hq)
  b= heapq.heappop(hq)
  s= a+b
  ans+=s
  heapq.heappush(hq,s)
  
print(ans)