# 2503

# 세자리 숫자 중 하나가 동일한 자리 위치하면 스트라이크, 숫자가 있지만 다른자리면 볼
# 3 스트라이크면 게임 끝 
# 가능한 답의 총 개수 구하기

n= int(input())
ask=[]
answer=[]

for _ in range(n):
  i= list(map(int, input().split()))
  ask.append(i[0])
  answer.append([i[1],i[2]])



# 재귀를 멈추는 조건은 answer이 끝났을 때, 
# 경우의 수를 찾는 문제임. 즉 스트라이크면 하나 고정해보고 돌려보기, 


temp=[]