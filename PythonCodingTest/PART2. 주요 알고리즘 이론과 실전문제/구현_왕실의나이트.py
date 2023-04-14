dot=input()

steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

current_c= ord(dot[0])-int(ord('a'))+1 #ord(c) c의 숫자형 아스키코드를 반환
current_r=int(dot[1])
count=0
for step in steps:
  nr=current_r+step[0]
  nc=current_c+step[1]
  if(0<nr<9 and 0<nc<9):
    count+=1
    
print(count)