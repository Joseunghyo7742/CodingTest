'''
오르막수 

수의 길이 N이 주어졌을 때, 오르막 수의 개수를 구하는 프로그램
'''

n= int(input())
dp=[
  [1]*10,
]

for i in range(1,n): # 자리수 순차
  tmp=[0]*10
  for j in range(0,10): 
    t=0
    for k in range(j+1):
      t+=dp[i-1][k]
    tmp[j]=t
  dp.append(tmp)
print(sum(dp[-1])%10007)

