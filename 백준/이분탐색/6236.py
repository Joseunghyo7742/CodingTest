# 용돈관리
# 출력: 통장에서 인출해야할 최소금액 k 
'''
통장에서 K원을 인출하며,
통장에서 뺀 돈으로 하루를 보낼 수 있으면 그대로 사용하고
모자라게 되면 남은 금액은 통장에 집어넣고 다시 K원을 인출
정확히 M번을 맞추기 위해서 남은 금액이 그날 사용할 금액보다 많더라도 남은 금액은 통장에 집어넣고 다시 K원을 인출할 수 있다
'''



# 최소금액을 찾는 것.
def binary_search():
  st = max(money) # 최소 인출 금액은 하루 중 가장 많이 쓰는 금액이어야 함, 왜냐면 그 이하면 인출해도 지출불가이기 때문
  en= sum(money) # 최대 인출 금액은 모든 날 합친 것 

  result= en

  while(st<=en):
    mid= (st+en)//2  # 인출할 금액
    curr=0 # 현재 가지고있는 금액
    deposit=0 # 인출횟수
    
    for k in money: # 날짜별 금액
      if curr < k: # 돈이 부족하면 새로 인출
        deposit+=1
        curr=mid
      curr-=k #가지고있는 돈에서 빼기 
    
    if deposit>m:
      st= mid+1 # mid보다 더 큰 돈을 인출해야 함
    else: # 인출 횟수가 작거나 같을 떄
      result= mid # mid는 조건을 만족함
      en= mid-1 # 더 작은 경우도 만족할지 확인 
  return result

n,m= map(int,input().split()) #n일 동안 사용, M번만 인출
money=[] # i번째날 이용할 금액 
for _ in range(n):
  money.append(int(input()))

print(binary_search())