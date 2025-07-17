# 2961_백트래킹 
# 인풋: 재료 개수, 재료의 [신맛, 쓴맛]
# 신맛은 곱하고 쓴맛은 합한다
# 아웃풋: 신맛과 쓴맛의 차이가 가장 작은 요리 만들기

# 재료를 돌면서 맛의 차이를 구한다
# 맛의 차이가 가장 적은 걸 저장한다

def get_flavor_diff(idx, sour, bitter,count):
  global answer
  if(idx==n):
    if(count==0):
      return
    diff= abs(sour-bitter)
    answer= min(diff,answer)
    return answer
  
  #재료를 넣는 경우
  get_flavor_diff(idx+1,sour*ingre[idx][0], bitter+ingre[idx][1],count+1)
  
  #재료를 넣지않는 경우
  get_flavor_diff(idx+1, sour, bitter,count)
  
answer= 1_000_000_000
n= int(input())
ingre= [list(map(int,input().split())) for _ in range(n)]

get_flavor_diff(0,1,0,0)
print(answer)