'''
치킨 배달
푼 날짜: 25.09.09

치킨거리: 집에서 가장 가까운 치킨집거리
도시의 치킨거리: 모든 집의 치킨거리 합

거리 구하기 : 임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|

0은 빈 칸, 1은 집, 2는 치킨집

m개의 치킨집만 남기고 폐업할건데 이때 도시의 치킨거리가 최소가 되도록하기 
'''
import sys
from itertools import combinations

input= sys.stdin.readline

n,m= map(int,input().split())
city=[]
stores=[]
homes=[]
for _ in range(n):
  city.append(list(map(int,input().split())))

# 집과 치킨집 위치 저장
for i in range(n):
  for j in range(n):
    if(city[i][j]==1):
      homes.append((i,j))
    elif(city[i][j]==2):
      stores.append((i,j))


result= 9999
# 폐업할 치킨집 조합
for comb in combinations(stores,m):
  total=0
  for h in homes:
    if(total>= result): 
      break
    min_distance=9999
    for c in comb:
      min_distance=min(min_distance,abs(h[0]-c[0])+abs(h[1]-c[1]))
    total+=min_distance
  result= min(result, total)

print(result)