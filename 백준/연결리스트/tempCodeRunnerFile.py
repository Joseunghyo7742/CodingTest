# 영어 소문자만 최대 600,000글자
# 커서 문장 맨 앞/ 문장 맨 뒤/ 문장 중간 임의의 곳 

#입력: 편집기에 입력된 문자열/ 그 이후 입력된 명령어
#출력: 편집기에 입력되어 있는 모든 문자열
import sys
input= sys.stdin.readline

line= list[input().strip()]
line2=[] #커서의 오른쪽에 위치한 것들, 거꾸로 스택 
n= int(input())

for _ in range(n):
  indi= input().split()
  
  if indi[0]=="L" and line: #커서 왼쪽에 값이 있다면 빼주고 스택2에 넣기 
    line2.append(line.pop())
  elif indi[0]=="D" and line2: #커서 오른쪽 값이 있다면 빼주고 스택으로 넣기
    line.append(line2.pop())
  elif indi[0]=="B" and line:
    line.pop()
  elif indi[0]=="P":
    line.append(indi[1])

line.extend(reversed(line2))
print(''.join(line))