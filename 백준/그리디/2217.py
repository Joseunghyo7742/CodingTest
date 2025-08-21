'''
로프
푼 날짜: 25.08.21

로프의 정보가 주어졌을 때 
로프들을 이용해 들어올릴 수 있는 물체의 최대 중량 구하기 

최대 중량!! 

10 15
중량 10 -> 10/2 => 5씩 걸림
중량 15 -> 15/2 => 7.5
중량 20 -> 20/2 => 10씩 

로프 중 가장 최소가 되는 값, 
각로프에 걸릴것 =w/k 

약한 로프를 끼우면 전체 하중 한도가 내려가니, 강한 로프 몇 개만 쓰는 편이 유리할 수 있어요.
10 20 30 20
30 20 20 10 => 40
30 20 20 => 60
30 20 => 40
'''
import sys

input= sys.stdin.readline

n= int(input())
w=[]
for _ in range(n):
  w.append(int(input()))

w.sort()

tmp=0
for i in range(n):
  tmp= max(tmp, w[i]*(n-i))

print(tmp)
  
  