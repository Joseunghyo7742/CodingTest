'''
좌표 정렬하기
푼 날짜: 25.09.03
'''
n= int(input())
points=[]
for _ in range(n):
  points.append(list(map(int,input().split())))

points.sort(key= lambda x: (x[0],x[1]))

for k in points:
  print(* k)