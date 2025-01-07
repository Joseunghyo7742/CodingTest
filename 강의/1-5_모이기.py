# n명의 학생이 모이는데  (n>=1)
# 1,2, 3, ...n명이 모이는데 각각의 최소거리비용


# 1번 아이디어
# X,y를 구한다음 거리를 구한다 
# 각 경우의 수에서 최소 값을 구한다

n= int(input())
d=[ list(map(int,input().split())) for _ in range(n)]
answer=[-1]*n

for x in range (1,1_001):
  for y in range (1,1_001):
    distance=[] 
    for item in d:
      a,b=item # 위치
      distance.append(abs(a-x)+abs(b-y))

    # 가까운 순 배치
    distance.sort()
    
    tmp=0
    # 한명, 두명, 세명, n명 모일때 최소값을 더해주어야 함.
    for i in range(len(distance)):
      di= distance[i]
      tmp+=di
      if(answer[i]==-1):
        answer[i]=tmp
      else:
        answer[i]= min(tmp, answer[i])
        

print(*answer)
    
    
      