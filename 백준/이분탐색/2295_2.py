

"""
### N(5 ≤ N ≤ 1,000)개의 자연수들로 이루어진 집합 U가 있다.
###  세 수의 합 d도 U안에 포함되는 경우가 있을 수 있다

find biggest d

U의 원소는 200,000,000보다 작거나 같은 자연수이다

U 배열에 원소 저장
Uposi 배열에 원소=index가 되도록 1을 저장

1. U에서 자연수 3개 고르기  => NC3 = N(N-1)(N-2)/3 = O[N^3] ~= 1억회 수행 ~= 1초
2. 합이 U 안에 있는 지 찾기 => Uposi 배열로 O[1]
3. 가장 큰 값을 update하기
"""



n= int(input())
U=[] # U원소는 200_000_000이하 자연수 
Uposi = [0]*200000004

for _ in range(n):
  temp = int(input())
  U.append(temp)
  Uposi[temp] = 1

answer = -1
  
# cnt개가 arr에 들어있어서 (3-cnt)회만 붙여준다. idx 전까지는 탐색했으니 앞으로 찾자
def combi(cnt, idx, arr):  
  global answer
  # 3개 합산이 Uposi에 있는지 찾기
  if(cnt==3):
    #print(arr)
    temp = sum(arr)
    # 존재 체크
    if(Uposi[temp] == 1):
      answer = max(answer, temp)
    return
  
  # U 중에 하나 찾기
  for i in range(idx, len(U)):
    arr.append(U[i])
    combi(cnt+1, i+1, arr)
    arr.pop()
  

combi(0, 0, [])
print(answer)