# 2304 ,14719
n= int(input())
pillars=[]
for _ in range(n):
  pillars.append(list(map(int,input().split())))


# pillars.sort((key=lambda x:x[0]))
pillars.sort()

# 최대 높이인 기둥
highest= -1
high_idx=-1
for i in range(n):
  if pillars[i][1]>highest:
    highest= pillars[i][1]
    high_idx= i


# 양 방향에서 최대 높이인 지점까지 양방향으로 면적으로 구한다.
result=highest # 젤 높은 기둥 높이 저장 후 시작

prev= pillars[0][1]
for i in range(high_idx):
  if prev < pillars[i+1][1]:
    result+= prev*(pillars[i+1][0]-pillars[i][0])
    prev= pillars[i+1][1]
  else:
    result+= prev*(pillars[i+1][0]-pillars[i][0])

prev= pillars[-1][1]
for i in range(n-1, high_idx,-1):
  if prev<pillars[i-1][1]:
    result+= prev*(pillars[i][0]-pillars[i-1][0])
    prev= pillars[i-1][1]
  else:
    result+= prev*(pillars[i][0]-pillars[i-1][0])

print(result)