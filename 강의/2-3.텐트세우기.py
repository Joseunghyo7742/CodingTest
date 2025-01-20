# 2304 ,14719
n= int(input())
pillars=[]
for _ in range(n):
  pillars.append(list(map(int,input.split())))


pillars.sort((key=lambda x:x[0]))


# 양 방향에서 최대 높이인 지점까지 양방향으로 면적으로 구한다.
