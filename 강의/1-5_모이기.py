# n명의 학생이 모이는데  (n>=1)
# 1,2, 3, ...n명이 모이는데 각각의 최소거리비용


# 1번 아이디어
# X,y를 구한다음 거리를 구한다 
# 각 경우의 수에서 최소 값을 구한다

# n= int(input())
# d=[ list(map(int,input().split())) for _ in range(n)]
# answer=[-1]*n

# for x in range (1,1_001):
#   for y in range (1,1_001):
#     distance=[] 
#     for item in d:
#       a,b=item # 위치
#       distance.append(abs(a-x)+abs(b-y))

#     # 가까운 순 배치
#     distance.sort()
    
#     tmp=0
#     # 한명, 두명, 세명, n명 모일때 최소값을 더해주어야 함.
#     for i in range(len(distance)):
#       di= distance[i]
#       tmp+=di
#       if(answer[i]==-1):
#         answer[i]=tmp
#       else:
#         answer[i]= min(tmp, answer[i])
        

# print(*answer)
    
    

# 2번 아이디어 
# 우리의 집 중 한 곳에서 모인다.
# 그 점에서 가까운 사람만 더해주자
# 각 집에서 다른 집까지의 거리들을 배열로 두기
# 오름차순 정렬 후, n명 모였을 때 각각 배열에서 n번째합의 최소값

n= int(input())
# home=[list(map(int,input().split())) for _ in range(n)]

x=[]
y=[]
arr=[]

answer=[-1]*n
for _ in range(n):
  a,b= map(int,input().split())
  x.append(a)
  y.append(b)
  arr.append([a,b])
  
  
for i in x:
  for j in y:
    dist=[]
    
    for a,b in arr:
      d= abs(i-a)+abs(j-b)
      dist.append(d)
      
    dist.sort()
    
    tmp=0
    for i in range(len(dist)):
      d= dist[i]
      tmp+=d
      if answer[i]==-1:
        answer[i]= tmp
      else:
        answer[i]= min(tmp, answer[i])

