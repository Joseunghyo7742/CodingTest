# 동전 0 
# 가치의 합을 k로 만드려할때 필요한 동전 개수의 최솟값
# 오름차순으로 주어짐.


# D[i]= 가치의 합을 i로 만들 때 필요한 동전 개수의 최솟값
# D[i] = min(D[i-a1, D[i-A2],...]) - 시간초과
# 높은 가치의 동전을 우선 사용하려고 한다.

n,k= map(int,input().split()) 
values=[]
for _ in range(n):
  values.append(int(input()))

cnt=0

for i in range(n)[::-1]:
  if(k==0):
    break
  if(k>=values[i]):
    cnt+= k//values[i]
    k= k%values[i]

print(cnt)