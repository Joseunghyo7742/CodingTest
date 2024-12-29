#n+1일째 퇴사, n일간 상담
# T(i) 상담 기간, P(i) 금액
# 최대 수익
n= int(input())
tp= [[0,0]]
for i in range(n):
  tp.append(list(map(int,input().split())))

print(tp)
#i번째 일까지 일했을 떄 얻을 최대 수익
dp=[0 for i in range(n+1)]


for i in range(1,n+1):
  for j in range(i+tp[i][0]-1,n+1):
    if dp[j]<dp[i]+tp[i][1]:
      dp[j]= dp[i]+tp[i][1]
print(dp)
print(dp[-1])

# for i in range(n):
#   for j in range(i+tp[i][0],n+1):
#     if dp[j]< dp[i] + tp[i][1]:
#       dp[j] = dp[i]+ tp[i][1]  

# print(dp[-1])