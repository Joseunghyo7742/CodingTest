# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.

# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.


n= int(input())
track=[[0],[1]]

for i in range(2,n+1):
  temp=[i]
  prev= track[i-1]
  if(i%2==0):
    a= track[i//2]
    if(len(prev)>len(a)):
      prev=a
  if(i%3==0):
    b= track[i//3]
    if(len(prev)>len(b)):
      prev=b
  temp.extend(prev)
  track.append(temp)
  

print(len(track[n])-1)
print(*track[n])