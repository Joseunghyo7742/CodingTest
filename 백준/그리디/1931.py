'''
회의실배정
푼 날짜: 25.08.21

회의가 겹치지 않게 회의실을 사용할 수 있는 회의의 최대 개수 구하기

'''
import sys

input= sys.stdin.readline

n= int(input()) #회의 수
meeting=[]
for _ in range(n):
  meeting.append(list(map(int,input().split()))) # 시작시, 끝시 

meeting.sort(key=lambda x:(x[1],x[0]))

cnt=1
# 정렬한 뒤, 가장 먼저 끝나는 회의를 선택.
endTime= meeting[0][1]
for k in range(1,n):
  if(meeting[k][0]>= endTime):
    cnt+=1
    endTime= meeting[k][1]

print(cnt)