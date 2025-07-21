# 14501 퇴사
# T 상담시간, P 금액, 하루에 상담 하나, N+1 일째 퇴사
# 인풋: n , 1~n일까지 t,p
# 요구사항: 최대 수익
# 아웃풋: 최대 수익


def recur(day, cost):
  global max_profit
  
  if(day==n):
    max_profit= max(max_profit, cost)
    return
  
  # day에 상담하는 경우
  td,tc= counsel[day]
  if(day+td<=n):
      recur(day+td, cost+tc)
      
  #해당 일에 상담 안잡는 경우 
  recur(day+1,cost)
  

n= int(input())
counsel= [list(map(int,input().split())) for _ in range(n)]

max_profit= -1

recur(0,0)
print(max_profit)
# 1일 4일 5일 / 1일 5일 / 1일 6일 
# 제외:T를 더했을 때 N일을 초과하는 경우 


