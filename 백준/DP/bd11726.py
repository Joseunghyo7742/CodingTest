# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는
# 방법의 수를 10,007로 나눈 나머지 출력 
n= int(input())

d=[1,1]

for i in range(1,n):
  temp= d[i-1]+d[i]
  d.append(temp)

print(d[n]%10007)


