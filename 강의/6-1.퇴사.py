# DP 메모이제이션으로 풀기

def recur(idx):  
  if idx==n:
    return 0
  if idx > n:
    return -99999999

  if dp[idx] != -1: #이미 저장되어있다면 계산 스킵 
    return dp[idx]
  
  #상담을 받거나 안받거나 이 중 더 큰값을 저장 
  dp[idx]= max(recur(idx+counsel[idx][0])+ counsel[idx][1] , recur(idx+1))

  return dp[idx]

n= int(input())
counsel= [list(map(int,input().split())) for _ in range(n)]
dp= [-1 for _ in range(n)]

recur(0)
print(max(dp))