# 12865 평범한 배낭
# 입력: 물품의 수- 버틸 수 있는 무게 / 물건 무게&가치
# 출력: 물건의 가치 합 최대
# 무게 제한이 있음.


def recur(idx, weight ,value):
  global max_value
  
  if (weight> limit):
      return
  if(idx==n):
      max_value= max(max_value, value)
      return
  
  #물건을 넣느냐
  tw,tv= stuffs[idx]
  
  recur(idx+1,weight+tw, value+tv)
  #마느냐
  recur(idx+1, weight,value)

n, limit= map(int,input().split())
stuffs=[list(map(int,input().split())) for _ in range(n)]

max_value= -1
recur(0,0,0)

print(max_value)