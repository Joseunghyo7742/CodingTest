# 쉬운 계단수



# dp[n][i] n의 자리 수의 마지막 수가 i 일 때 경우의 수
n= int(input())
dp= [
  [0,0,0,0,0,0,0,0,0,0],
  [0,1,1,1,1,1,1,1,1,1], # 1의 자리 수일때
]

if(n>1):
  for i in range(1,n):
    n_stairs=[0]*10
    n_stairs[0]= dp[i][1]
    n_stairs[9]= dp[i][8]
    for j in range(1,9):
        n_stairs[j] = dp[i][j-1]+dp[i][j+1]
    
    dp.append(n_stairs)

  print(sum(dp[-1])% 1_000_000_000)
else:
  print(9)