# # 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# # 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# # 마지막 도착 계단은 반드시 밟아야 한다.
# 입력의 첫째 줄에 계단의 개수가 주어진다.
# 둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 
# 계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.

n= int(input())
stairs=[]

for _ in range(n):
  stairs.append(int(input()))

d=[[0,0],[stairs[0],stairs[0]]]  

for i in range(2,n+1):
  a= max(d[i-2][1], d[i-2][0]) + stairs[i-1]
  b= d[i-1][0] +stairs[i-1]
  d.append([a,b])

print(max(d[n][0],d[n][1]))
