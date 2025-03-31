# 2503

# 세자리 숫자 중 하나가 동일한 자리 위치하면 스트라이크, 숫자가 있지만 다른자리면 볼
# 3 스트라이크면 게임 끝 
# 가능한 답의 총 개수 구하기
# 서로 다른 수로 구성됨 -> 


n= int(input())
ask=[]
answer=[]
result=0

for _ in range(n):
  i= list(map(int, input().split()))
  ask.append(i[0])
  answer.append([i[1],i[2]])

def curr(i):
  # 재귀함수 -> answer에서 가능한 모든 경우의 수를 넣어본 후 가지를 뻗어보자
  if(i==n and temp.count(0)==0):
    result+=1
  # 스트라이크, 볼 경우의 수 전부
  s,b= answer[i]
  for k in ask[i]:
    
    
    
temp=[0,0,0]