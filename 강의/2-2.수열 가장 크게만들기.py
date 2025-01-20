# 1912

N = int(input())
arr= list(map(int,input().split()))

prefix=[arr[0]] # 누적합

for i in range(1,N):
  np= prefix[i-1]+ arr[i]
  prefix.append(max(np, arr[i]))

print(max(prefix))
