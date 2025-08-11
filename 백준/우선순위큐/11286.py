'''
절댓값 힙
푼 날짜: 8/9

입력: 연산의 개수 n, n개의 x값. x가 0이면 출력, 0이 아니면 배열에 넣음 
출력: x가 0일 때 배열에서 절댓값이 가장 작은 값 출력 (절댓값 같으면 가장 작은 수) & 배열에서 제거 / 배열이 빈 상태에서 출력해야하면 0 

'''

import sys
import heapq

input= sys.stdin.readline

num= int(input())
heap=[]

for i in range(num):
  x= int(input())
  if x!=0:
    heapq.heappush(heap, (abs(x),x))
  else:
    if len(heap) >0:
      min= heapq.heappop(heap)
      print(min[1])
    else:
      print(0)



