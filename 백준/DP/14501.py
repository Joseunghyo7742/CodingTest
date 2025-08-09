'''
퇴사
푼날짜: 8/8

출력: 최대 이익 출력하기 = 퇴사 전날까지 상담 코스트 높은 상담들 최대한 많이잡기
'''

# 해당 날짜에 상담했을 떄 최대 코스트
def dp(day,cost):
  global result
  #퇴사날을 초과하면 리턴 (상담 못함)
  if(day>n):
    return
  #퇴사날이다 코스트 최대값인지 비교하기 
  if(day==n):
    result= max(result, cost)
    return
  #이 날짜에 상담하는 경우 => 상담시간 걸린만큼 더한 후 재귀
  dp(day+tp[day][0], cost+tp[day][1])
  #이 날짜에 상담안하는 경우 => 다음 날로 가기
  dp(day+1, cost)

n= int(input())
tp=[list(map(int,input().split())) for _ in range(n)] # 0-time, 1- cost

result=-1
dp(0,0)
print(result)