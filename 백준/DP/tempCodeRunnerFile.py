'''
RGB거리
푼 날짜: 25.08.20

인접한 집 색은 달라야함
빨/초/파 로 칠하는 비용
최소 비용 구하기

집 개수는 1000까지
'''

import sys
input= sys.stdin.readline


n= int(input())
cost=[]

for _ in range(n):
  cost.append(list(map(int,input().split())))

  

dp=[[0]*n for _ in range(n)]
# dp[i][c] i번째 집을 c색으로 칠했을 때, 0~i번쨰 집까지의 최소 비용

dp[0]= cost[0]
for i in range(1,n):
  for j in range(3):
    dp[i][j]=cost[i][j]+min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])
  

print(min(dp[n-1]))