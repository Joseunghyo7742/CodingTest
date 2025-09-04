'''
회의실
푼 날짜: 25.09.03
회의가 겹치지 않으면서 회의실을 사용할 수 있는 회의 최대 개수 
'''

n= int(input())
meetings=[]
for _ in range(n):
  meetings.append(list(map(int,input().split())))

meetings.sort(key=lambda x: (x[1],x[0]))

result=0
last= 0
for k in meetings:
  st,ed=k[0],k[1]
  if(st>= last):
    last= ed
    result+=1
print(result)