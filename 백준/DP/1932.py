# 정수 삼각형
# 입력: 삼각형 크기 / 정수 삼각형
# 출력: 위에서부터 내려 올 때 최대 합


n= int(input())
tri= [list(map(int,input().split())) for _ in range(n)]

# tri[k][j]를 선택했다면 tri[k-1][j]와 tri[k-1][j-1]중 최대값을 더한다.
# 이때 주의할점은 양끝 인덱싱 오버하는 문제

dp=[[0]*n  for _ in range(n)]
dp[0]=tri[0]

for k in range(1,n):
  for j in range(k+1):
    if(j==0):
      dp[k][j]= tri[k][j]+dp[k-1][j]
    elif(j==k):
      dp[k][j]+= tri[k][j]+dp[k-1][j-1]   
    else:
      dp[k][j]= tri[k][j]+max(dp[k-1][j], dp[k-1][j-1])

print(max(dp[n-1]))