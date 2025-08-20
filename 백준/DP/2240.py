'''
자두나무
푼 날짜: 25.08.19

t초 동안 w번 움직일 수 있을 때, 최대 받을 수 있는 자두의 수 

'''

t,w = map(int,input().split())
data = [0] + [int(input()) for _ in range(t)]
dp = [[0 for _ in range(w+1)] for _ in range(t+1)] # t초 때, w 움직임 횟수일 때의 최대 자두 개수

for i in range(1,t+1): # t초만큼 돌기
  # 안움직일 때 처리 (초기값)
    if data[i]==1: # i초 때 1번 나무
      dp[i][0] = dp[i-1][0]+1 
    else: # i초 때 2번 나무
      dp[i][0] = dp[i-1][0] 
    
    
    for j in range(1,w+1): # 움직일 때 
        # 1번 나무에 떨어지는데 1번나무에 있음, 2번 나무에 떨어지는데 2번나무에 있음 
        if (data[i]==1 and j%2==0) or (data[i]==2 and j%2!=0):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])+1  # 직전 상태에서 이동 안 함(dp[i-1][j])과 이동 함(dp[i-1][j-1])
        else: # 1번 나무 떨어짐 2번나무에 있음, 2번 나무 떨어짐 1번 나무에 있음 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) # 직전 상태에서 이동 안 함(dp[i-1][j])과 이동 함(dp[i-1][j-1])
print(max(dp[t]))
