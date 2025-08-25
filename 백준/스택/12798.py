'''
도키도키 간식드리미
푼 날짜: 25.08.25

번호 표 대로 사람들이 간식을 받을 수 있도록 만들기
'''

import sys
input= sys.stdin.readline

n= int(input())
line= list(map(int,input().split()))

target=1
stack=[]

for k in line:
  # 번호표 타겟과 다르다면, 스택에 쌓여있는 맨 위 확인해보기
  while(stack and stack[-1]==target):
    stack.pop()
    target+=1
  if(k == target):
    target+=1
  else:
    stack.append(k)


#target이 n+1이 아니면 stack에 쌓은걸 순서대로 뽑아보고, 순차적으로 target과 맞다면 Nice
while(stack and stack[-1]==target):
  stack.pop()
  target+=1

if(target==(n+1)):
  print("Nice")
else:
  print("Sad")