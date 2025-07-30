# sort사용시 메모리 초과
# 카운트 정렬 풀어보자
# O(n)시간 : n개 정수를 리스트의 인덱스로 접근해 개수 세기 + 인덱스 출력 
import sys

input= sys.stdin.readline

n= int(input())
count=[0]*10001

for _ in range(n):
  tmp=int(input())
  count[tmp]+=1


for i in range(1,10_001):
  if(count[i]>0):
    while(count[i]!=0):
      print(i)
      count[i]-=1

