'''
1,2,3 더하기
푼날짜:25.08.18
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수

1 =1 
2= 1+1, 2  
3= 1+1+1, 1+2, 2+1, 3    4
4= 1+1+1+1, 1+2+1, 2+1+1, 3+1, 1+1+2, 2+2, 1+3    7
5= 5?? nono 


'''
import sys
input= sys.stdin.readline
t= int(input())

d=[0]*12
d[1]=1
d[2]=2
d[3]= 4

for i in range(4,12):
  d[i]= d[i-1]+d[i-2]+d[i-3]

for _ in range(t):
  n= int(input())
  print(d[n]) 
