# RGB거리
# 인풋: 집 수, R/G/B 칠하는 비용 집들
# 아웃풋: 모든 집 칠하는 비용 최솟값

#조건 => 인접한 집들과 색이 같지않게 
  # 1번집 != 2번집
  # n번집 != n-1번집
  # i(2<=i<=n-1) 집 != i-1, i+1
  
n= int(input())
homes=[list(map(int,input().split())) for _ in range(n)]

# 이전 집에서 칠한 걸 칠하지 않는다.
dp =[[0]*3 for _ in range(n)]
dp[0]=homes[0] # 첫행 비용은 그대로

for i in range(1,n):
  for j in range(3):
    dp[i][j]= homes[i][j]+ min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])

print(min(dp[n-1]))