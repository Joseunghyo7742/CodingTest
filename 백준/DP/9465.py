'''
스티커
푼 날짜: 25.09.12

스티커 떼면 왼,오,위,아래 같이 떼짐
2n개의 스티커 중에서 점수의 합이 최대가 되면서 서로 변을 공유 하지 않는 스티커 집합
    1  2  3  4 5
위   0  0  0
아래 0  0   0
선택안함
[
  [],
  [],
  [],
]
'''


    
t= int(input())
for _ in range(t):
  n= int(input())
  stickers=[]
  for _ in range(2):
    stickers.append(list(map(int,input().split())))

  dp=[[0]*n for _ in range(3)]
  


  # dp[0][j] = j열 위 선택
  # dp[1][j] = j열 아래 선택
  # dp[2][j] = j열 선택 안함
  dp = [[0]*n for _ in range(3)]

  dp[0][0] = stickers[0][0]
  dp[1][0] = stickers[1][0]
  dp[2][0] = 0

  for j in range(1, n):
      dp[0][j] = stickers[0][j] + max(dp[1][j-1], dp[2][j-1])
      dp[1][j] = stickers[1][j] + max(dp[0][j-1], dp[2][j-1])
      dp[2][j] = max(dp[0][j-1], dp[1][j-1], dp[2][j-1])

  print(max(dp[0][n-1], dp[1][n-1], dp[2][n-1]))