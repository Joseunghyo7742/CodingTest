'''
구간합구하기4
푼 날짜: 25.08.28
'''
import sys

input = sys.stdin.readline
n,m= map(int,input().split())
arr=list(map(int,input().split()))
sum_arr=[0]

for i in range(0,n):
  sum_arr.append(sum_arr[i]+arr[i])

for _ in range(m):
  i,j= map(int,input().split())
  print(sum_arr[j]-sum_arr[i-1])
  