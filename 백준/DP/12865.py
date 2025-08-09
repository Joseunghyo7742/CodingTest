'''
평범한 배낭
푼날짜: 8/8
출력: 물건 가치합의 최대값
'''

#idx번째 물건부터, 현재 배낭 무게가 weight일 때 담을 수 있는 최대 가치
def getMaxValue(idx, weight):
  if weight > k:
    return -9999
  if idx == n:
    return 0
  if dp[idx][weight] != -1:
    return dp[idx][weight]

  dp[idx][weight] = max(
    getMaxValue(idx + 1, weight + stuffs[idx][0]) + stuffs[idx][1],
    getMaxValue(idx + 1, weight)
  )
  return dp[idx][weight]

n, k = map(int, input().split())  # 물건 수, 배낭 무게 제한
stuffs = [list(map(int, input().split())) for _ in range(n)]  # [무게, 가치]

dp = [[-1] * (k + 1) for _ in range(n )]  #  i번째 물건부터 시작했을 때, 현재 무게가 w일 때 얻을 수 있는 최대 가치

print(getMaxValue(0, 0))
